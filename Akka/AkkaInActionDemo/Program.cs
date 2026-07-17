using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Linq;
using System.Threading.Tasks;
using Akka;
using Akka.Actor;
using Akka.Event;
using Akka.TestKit;
using Akka.TestKit.Xunit2;
using Xunit;

namespace AkkaInActionDemo
{
    // ============================================================
    // 1. ОПРЕДЕЛЕНИЕ СООБЩЕНИЙ (аналогично case class в Scala)
    // ============================================================

    // Сообщения для актора TicketSeller (продавец билетов)
    public static class TicketSellerMessages
    {
        // Команда: добавить билеты в продажу
        public class AddTickets
        {
            public IReadOnlyList<Ticket> Tickets { get; }
            public AddTickets(IReadOnlyList<Ticket> tickets) => Tickets = tickets;
        }

        // Команда: купить N билетов
        public class BuyTickets
        {
            public int Count { get; }
            public BuyTickets(int count) => Count = count;
        }

        // Команда: запросить текущее событие
        public class GetEvent { }

        // Команда: отменить событие (продажу)
        public class Cancel { }

        // Ответ: список купленных билетов
        public class TicketsSold
        {
            public string EventName { get; }
            public IReadOnlyList<Ticket> Entries { get; }
            public TicketsSold(string eventName, IReadOnlyList<Ticket> entries)
            {
                EventName = eventName;
                Entries = entries;
            }
        }

        // Модель билета
        public class Ticket
        {
            public int Id { get; }
            public Ticket(int id) => Id = id;
        }
    }

    // Сообщения для актора BoxOffice (касса)
    public static class BoxOfficeMessages
    {
        public class GetAllEvents { }

        // Команда: создать новое событие
        public class CreateEvent
        {
            public string Name { get; }
            public int TicketCount { get; }
            public CreateEvent(string name, int ticketCount)
            {
                Name = name;
                TicketCount = ticketCount;
            }
        }

        // Команда: запросить событие по имени
        public class GetEvent
        {
            public string Name { get; }
            public GetEvent(string name) => Name = name;
        }

        // Команда: купить билеты на событие
        public class BuyTickets
        {
            public string EventName { get; }
            public int Count { get; }
            public BuyTickets(string eventName, int count)
            {
                EventName = eventName;
                Count = count;
            }
        }

        // Команда: отменить событие
        public class CancelEvent
        {
            public string Name { get; }
            public CancelEvent(string name) => Name = name;
        }

        // Ответ: событие создано
        public class EventCreated
        {
            public string Name { get; }
            public int TicketCount { get; }
            public EventCreated(string name, int ticketCount)
            {
                Name = name;
                TicketCount = ticketCount;
            }
        }

        // Ответ: событие уже существует
        public class EventExists { }

        // Ответ: информация о событии
        public class EventInfo
        {
            public string Name { get; }
            public int TicketsLeft { get; }
            public EventInfo(string name, int ticketsLeft)
            {
                Name = name;
                TicketsLeft = ticketsLeft;
            }
        }

        // Ответ: список всех событий
        public class AllEvents
        {
            public IReadOnlyList<EventInfo> Events { get; }
            public AllEvents(IReadOnlyList<EventInfo> events) => Events = events;
        }
    }

    // ============================================================
    // 2. АКТОРЫ
    // ============================================================

    // Актор-продавец билетов для одного события
    public class TicketSellerActor : ReceiveActor
    {
        // Состояние актора: список доступных билетов (ImmutableList – неизменяемая коллекция)
        private ImmutableList<TicketSellerMessages.Ticket> _tickets = ImmutableList<TicketSellerMessages.Ticket>.Empty;

        // Имя события, которое продаётся
        private readonly string _eventName;

        public TicketSellerActor(string eventName)
        {
            _eventName = eventName;

            // Определяем обработчики сообщений
            Receive<TicketSellerMessages.AddTickets>(msg =>
            {
                // Добавляем новые билеты в конец списка (ImmutableList.AddRange создаёт новый список)
                _tickets = _tickets.AddRange(msg.Tickets);
            });

            Receive<TicketSellerMessages.BuyTickets>(msg =>
            {
                // Берём первые N билетов
                var bought = _tickets.Take(msg.Count).ToImmutableList();
                if (bought.Count == msg.Count)
                {
                    // Удаляем купленные билеты из списка
                    _tickets = _tickets.RemoveRange(bought);
                    // Отвечаем отправителю (Sender) списком купленных билетов
                    Sender.Tell(new TicketSellerMessages.TicketsSold(_eventName, bought));
                }
                else
                {
                    // Недостаточно билетов – отправляем пустой список
                    Sender.Tell(new TicketSellerMessages.TicketsSold(_eventName, ImmutableList<TicketSellerMessages.Ticket>.Empty));
                }
            });

            Receive<TicketSellerMessages.GetEvent>(_ =>
            {
                // Отвечаем информацией о событии и количестве оставшихся билетов
                Sender.Tell(new BoxOfficeMessages.EventInfo(_eventName, _tickets.Count));
            });

            Receive<TicketSellerMessages.Cancel>(_ =>
            {
                // Отвечаем информацией о событии перед остановкой
                Sender.Tell(new BoxOfficeMessages.EventInfo(_eventName, _tickets.Count));
                // PoisonPill – специальное сообщение для остановки актора
                Self.Tell(PoisonPill.Instance);
            });
        }
    }

    // Актор-касса, управляющий продавцами билетов
    public class BoxOfficeActor : ReceiveActor
    {
        // Словарь дочерних акторов-продавцов (ключ – имя события)
        private readonly Dictionary<string, IActorRef> _ticketSellers = new Dictionary<string, IActorRef>();

        public BoxOfficeActor()
        {
            // Обработчик создания события
            Receive<BoxOfficeMessages.CreateEvent>(msg =>
            {
                if (_ticketSellers.ContainsKey(msg.Name))
                {
                    // Событие уже существует
                    Sender.Tell(new BoxOfficeMessages.EventExists());
                }
                else
                {
                    // Создаём дочернего актора-продавца с именем, равным имени события
                    var seller = Context.ActorOf(Props.Create(() => new TicketSellerActor(msg.Name)), msg.Name);
                    _ticketSellers[msg.Name] = seller;

                    // Генерируем билеты с Id от 1 до TicketCount
                    var tickets = Enumerable.Range(1, msg.TicketCount)
                                             .Select(id => new TicketSellerMessages.Ticket(id))
                                             .ToImmutableList();
                    seller.Tell(new TicketSellerMessages.AddTickets(tickets));

                    // Отвечаем, что событие создано
                    Sender.Tell(new BoxOfficeMessages.EventCreated(msg.Name, msg.TicketCount));
                }
            });

            // Обработчик покупки билетов
            Receive<BoxOfficeMessages.BuyTickets>(msg =>
            {
                if (_ticketSellers.TryGetValue(msg.EventName, out var seller))
                {
                    // Перенаправляем запрос продавцу, но ответ должен прийти напрямую отправителю,
                    // поэтому используем Forward (сохраняет оригинального отправителя)
                    seller.Forward(new TicketSellerMessages.BuyTickets(msg.Count));
                }
                else
                {
                    // Событие не найдено – отправляем пустой ответ
                    Sender.Tell(new TicketSellerMessages.TicketsSold(msg.EventName, ImmutableList<TicketSellerMessages.Ticket>.Empty));
                }
            });

            // Обработчик запроса информации о событии
            Receive<BoxOfficeMessages.GetEvent>(msg =>
            {
                if (_ticketSellers.TryGetValue(msg.Name, out var seller))
                {
                    seller.Forward(new TicketSellerMessages.GetEvent());
                }
                else
                {
                    Sender.Tell(null); // событие не найдено
                }
            });

            // Обработчик отмены события
            Receive<BoxOfficeMessages.CancelEvent>(msg =>
            {
                if (_ticketSellers.TryGetValue(msg.Name, out var seller))
                {
                    // Посылаем продавцу команду Cancel, он ответит информацией о событии
                    seller.Forward(new TicketSellerMessages.Cancel());
                    _ticketSellers.Remove(msg.Name);
                }
                else
                {
                    Sender.Tell(null);
                }
            });

            Receive<BoxOfficeMessages.GetAllEvents>(_ =>
            {
                var tasks = _ticketSellers.Values.Select(seller =>
                    seller.Ask<BoxOfficeMessages.EventInfo>(new TicketSellerMessages.GetEvent(), TimeSpan.FromSeconds(2)));
                Task.WhenAll(tasks).ContinueWith(t =>
                {
                    var infos = t.Result.Where(info => info != null).ToImmutableList();
                    return new BoxOfficeMessages.AllEvents(infos);
                }).PipeTo(Sender);
            });
        }

        // Дополнительное сообщение для запроса всех событий (добавлено здесь для удобства)
        public class GetAllEvents { }
    }

    // ============================================================
    // 3. ЗАПУСК ПРИЛОЖЕНИЯ
    // ============================================================

    class Program
    {
        static async Task Main(string[] args)
        {
            // 1. Создаём систему акторов (ActorSystem) – корневой контейнер для всех акторов
            //    Имя системы должно быть уникальным в пределах JVM/процесса.
            using (var system = ActorSystem.Create("GoTicksSystem"))
            {
                // 2. Создаём актор верхнего уровня BoxOffice через систему.
                //    Props – конфигурация для создания актора (указываем тип).
                var boxOffice = system.ActorOf(Props.Create<BoxOfficeActor>(), "boxOffice");

                // 3. Отправляем команду создания события "RHCP" с 10 билетами
                //    Используем Ask (запрос-ответ) для получения ответа синхронно (или асинхронно)
                var createResult = await boxOffice.Ask<BoxOfficeMessages.EventCreated>(
                    new BoxOfficeMessages.CreateEvent("RHCP", 10),
                    TimeSpan.FromSeconds(3));

                Console.WriteLine($"Событие создано: {createResult.Name}, билетов: {createResult.TicketCount}");

                // 4. Покупаем 2 билета на событие "RHCP"
                var buyResult = await boxOffice.Ask<TicketSellerMessages.TicketsSold>(
                    new BoxOfficeMessages.BuyTickets("RHCP", 2),
                    TimeSpan.FromSeconds(3));

                Console.WriteLine($"Куплено билетов: {buyResult.Entries.Count} на событие {buyResult.EventName}");

                // 5. Запрашиваем информацию о событии
                var eventInfo = await boxOffice.Ask<BoxOfficeMessages.EventInfo>(
                    new BoxOfficeMessages.GetEvent("RHCP"),
                    TimeSpan.FromSeconds(3));

                Console.WriteLine($"Осталось билетов на {eventInfo.Name}: {eventInfo.TicketsLeft}");

                // 6. Запрашиваем список всех событий
                var allEvents = await boxOffice.Ask<BoxOfficeMessages.AllEvents>(
                    new BoxOfficeMessages.GetAllEvents(),
                    TimeSpan.FromSeconds(3));

                Console.WriteLine("Все события:");
                foreach (var ev in allEvents.Events)
                {
                    Console.WriteLine($"  {ev.Name}: {ev.TicketsLeft} билетов");
                }

                // 7. Отменяем событие "RHCP"
                var cancelResult = await boxOffice.Ask<BoxOfficeMessages.EventInfo>(
                    new BoxOfficeMessages.CancelEvent("RHCP"),
                    TimeSpan.FromSeconds(3));

                if (cancelResult != null)
                    Console.WriteLine($"Событие {cancelResult.Name} отменено. Продано билетов: {cancelResult.TicketsLeft}");

                // 8. Останавливаем систему акторов (освобождаем ресурсы)
                await system.Terminate();
            }

            Console.WriteLine("Нажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }

    // ============================================================
    // 4. МОДУЛЬНЫЙ ТЕСТ (пример тестирования актора)
    // ============================================================

    // Класс теста должен быть в отдельном файле в проекте, но для компактности помещаем его здесь.
    // В реальном проекте тесты выносят в отдельную библиотеку.
    public class BoxOfficeActorTests : TestKit
    {
        [Fact]
        public void BoxOffice_should_create_event_and_sell_tickets()
        {
            // Создаём тестовую систему акторов (TestKit предоставляет ActorSystem)
            var boxOffice = Sys.ActorOf(Props.Create<BoxOfficeActor>(), "testBoxOffice");

            // 1. Создаём событие
            boxOffice.Tell(new BoxOfficeMessages.CreateEvent("TestEvent", 5));
            // Ожидаем ответ EventCreated
            var created = ExpectMsg<BoxOfficeMessages.EventCreated>();
            Assert.Equal("TestEvent", created.Name);

            // 2. Покупаем 3 билета
            boxOffice.Tell(new BoxOfficeMessages.BuyTickets("TestEvent", 3));
            var sold = ExpectMsg<TicketSellerMessages.TicketsSold>();
            Assert.Equal(3, sold.Entries.Count);

            // 3. Проверяем остаток (2 билета)
            boxOffice.Tell(new BoxOfficeMessages.GetEvent("TestEvent"));
            var info = ExpectMsg<BoxOfficeMessages.EventInfo>();
            Assert.Equal(2, info.TicketsLeft);
        }
    }
}