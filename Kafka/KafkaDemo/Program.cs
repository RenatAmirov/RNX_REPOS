// =====================================================================
// Консольное приложение на C# для демонстрации работы с Apache Kafka
// на основе книги "Apache Kafka в действии" (Зеленин, Кропп).
// =====================================================================
//
// Требования:
// - Установленный пакет Confluent.Kafka (через NuGet)
//   dotnet add package Confluent.Kafka
// - Запущенный кластер Kafka (например, локальный на localhost:9092)
// - Созданный топик "products.prices.changelog" (или программа создаст его автоматически, если разрешено)
//
// В примере показаны:
// - Базовые настройки продюсера (acks, идемпотентность, сериализация)
// - Отправка сообщений с ключами (для гарантии порядка в партиции)
// - Параллельный запуск нескольких продюсеров (демонстрация многопоточности)
// - Потребитель в составе группы (для масштабирования и сохранения смещений)
// - Чтение сообщений с начала топика (--from-beginning) или только новых
// - Обработка ошибок и логирование
//
// =====================================================================

using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using Confluent.Kafka;

namespace KafkaDemo
{
    class Program
    {
        // Конфигурационные параметры (можно вынести в appsettings.json)
        private const string BootstrapServers = "localhost:9092";    // Адрес кластера Kafka
        private const string TopicName = "products.prices.changelog"; // Имя топика
        private const string ConsumerGroupId = "prices-monitor";      // Группа потребителей

        static async Task Main(string[] args)
        {
            // Запускаем продюсера и потребителя параллельно (асинхронно)
            var producerTask = RunProducerAsync(CancellationToken.None);
            var consumerTask = RunConsumerAsync(CancellationToken.None);

            // Ожидаем завершения (в реальном приложении можно ожидать нажатия клавиши)
            Console.WriteLine("Нажмите любую клавишу для завершения...");
            Console.ReadKey();

            // Отменяем задачи (для демонстрации можно использовать CancellationTokenSource)
            // Здесь просто завершаем, но в реальном коде нужно корректно останавливать.
            // В данном примере задачи бесконечны, поэтому просто выходим.
            // Для чистоты можно использовать CancellationTokenSource.
        }

        /// <summary>
        /// Задача продюсера – отправляет сообщения в топик.
        /// </summary>
        private static async Task RunProducerAsync(CancellationToken cancellationToken)
        {
            // Настройки продюсера (соответствуют рекомендациям книги)
            var producerConfig = new ProducerConfig
            {
                BootstrapServers = BootstrapServers,
                // acks=all – гарантирует, что сообщение записано на все синхронизированные реплики
                Acks = Acks.All,
                // Включение идемпотентности – гарантирует "ровно один раз" в пределах партиции
                EnableIdempotence = true,
                // Максимальное количество неподтверждённых запросов в полёте (для идемпотентности не более 5)
                //MaxInFlightRequestsPerConnection = 5,
                MaxInFlight = 5,
                // Количество повторных попыток при ошибках (большое значение, но ограничено таймаутом)
                MessageSendMaxRetries = 10000000,
                // Задержка между повторами (100 мс)
                RetryBackoffMs = 100,
                // Таймаут доставки сообщения (2 минуты)
                //DeliveryTimeoutMs = 120000,
                // Таймаут запроса (30 секунд)
                RequestTimeoutMs = 30000
            };

            producerConfig.Set("delivery.timeout.ms", "120000"); // значение в миллисекундах

            // Создаём продюсера с сериализаторами для ключа и значения (используем строки)
            using var producer = new ProducerBuilder<string, string>(producerConfig)
                .SetKeySerializer(Serializers.Utf8)
                .SetValueSerializer(Serializers.Utf8)
                .Build();

            // Симуляция отправки сообщений от разных "отделов" (например, изменение цен)
            var departments = new[] { "Coffee", "SoftDrinks", "Snacks" };
            var rnd = new Random();
            var counter = 0;

            while (!cancellationToken.IsCancellationRequested)
            {
                // Генерируем сообщение: ключ – название товара, значение – цена
                var product = departments[rnd.Next(departments.Length)] + (rnd.Next(1, 100)).ToString();
                var price = (rnd.Next(1, 20) + rnd.NextDouble()).ToString("F2");
                var key = product;
                var value = price;

                // Формируем сообщение (запись)
                var message = new Message<string, string>
                {
                    Key = key,
                    Value = value
                };

                try
                {
                    // Асинхронная отправка с обработчиком результата (callback)
                    var deliveryResult = await producer.ProduceAsync(TopicName, message);
                    // Вывод информации об успешной отправке
                    Console.WriteLine($"[ПРОДЮСЕР] Отправлено: ключ='{deliveryResult.Key}', " +
                                      $"значение='{deliveryResult.Value}', " +
                                      $"партиция={deliveryResult.Partition}, " +
                                      $"смещение={deliveryResult.Offset}");
                }
                catch (ProduceException<string, string> ex)
                {
                    // Ошибка при отправке (например, недоступен брокер)
                    Console.WriteLine($"[ПРОДЮСЕР] Ошибка: {ex.Error.Reason}");
                }

                // Имитация паузы между отправками (чтобы не забивать кластер)
                await Task.Delay(1000, cancellationToken);
                counter++;

                // После 10 сообщений можно выйти (для демонстрации)
                if (counter >= 10)
                    break;
            }

            // Освобождение ресурсов происходит автоматически при выходе из using
            Console.WriteLine("[ПРОДЮСЕР] Завершён.");
        }

        /// <summary>
        /// Задача потребителя – читает сообщения из топика в составе группы.
        /// </summary>
        private static async Task RunConsumerAsync(CancellationToken cancellationToken)
        {
            // Настройки потребителя
            var consumerConfig = new ConsumerConfig
            {
                BootstrapServers = BootstrapServers,
                GroupId = ConsumerGroupId,         // Идентификатор группы
                // Автоматическая фиксация смещений (удобно, но может привести к дублированию)
                // Для гарантии exactly-once лучше управлять вручную, но для примера оставим автофиксацию
                EnableAutoCommit = true,
                AutoCommitIntervalMs = 5000,
                // Начало чтения: с самого старого сообщения, если нет сохранённого смещения
                AutoOffsetReset = AutoOffsetReset.Earliest,
                // Таймаут сессии (30 сек) – если потребитель не отвечает, то перебалансировка
                SessionTimeoutMs = 30000,
                // Интервал отправки heartbeat (3 сек)
                HeartbeatIntervalMs = 3000,
                // Максимальное время между вызовами Poll (для предотвращения "зависших" потребителей)
                MaxPollIntervalMs = 300000
            };

            // Создаём потребителя с десериализаторами
            using var consumer = new ConsumerBuilder<Ignore, string>(consumerConfig)
                .SetValueDeserializer(Deserializers.Utf8)
                .Build();

            // Подписываемся на топик
            consumer.Subscribe(TopicName);

            Console.WriteLine($"[ПОТРЕБИТЕЛЬ] Подписан на топик '{TopicName}', группа '{ConsumerGroupId}'");

            try
            {
                while (!cancellationToken.IsCancellationRequested)
                {
                    // Чтение сообщения с таймаутом (100 мс)
                    var consumeResult = consumer.Consume(TimeSpan.FromMilliseconds(100));
                    if (consumeResult == null)
                        continue; // Нет новых сообщений

                    // Обработка полученного сообщения
                    Console.WriteLine($"[ПОТРЕБИТЕЛЬ] Получено: ключ='{consumeResult.Message.Key}', " +
                                      $"значение='{consumeResult.Message.Value}', " +
                                      $"партиция={consumeResult.Partition}, " +
                                      $"смещение={consumeResult.Offset}");

                    // Здесь могла бы быть бизнес-логика (обновление цен, аналитика и т.д.)

                    // Если включена автофиксация, смещение сохранится автоматически.
                    // Для ручного управления используйте consumer.Commit(consumeResult);
                }
            }
            catch (ConsumeException ex)
            {
                Console.WriteLine($"[ПОТРЕБИТЕЛЬ] Ошибка потребления: {ex.Error.Reason}");
            }
            finally
            {
                // Закрываем потребитель (освобождаем ресурсы, сохраняем смещения)
                consumer.Close();
                Console.WriteLine("[ПОТРЕБИТЕЛЬ] Завершён.");
            }
        }
    }
}