using System;                           // Для базовых типов и консольного ввода-вывода
using System.Data;                       // Для работы с таблицами данных (DataTable)
using Npgsql;                            // Провайдер для подключения к PostgreSQL
using System.Threading.Tasks;            // Для асинхронных операций

namespace SQLFilteringDemo
{
    class Program
    {
        // Строка подключения к базе данных PostgreSQL
        // Замените параметры Host, Username, Password, Database на свои
        static string connectionString = "Host=localhost;Port=5432;Username=postgres;Password=Vozinja01234!;Database=testdb";

        static async Task Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;   // Поддержка русского текста в консоли

            // 1. Создаём демонстрационную таблицу и наполняем её тестовыми данными (если их нет)
            await SetupDatabaseAsync();

            // 2. Выполняем серию запросов, каждый из которых иллюстрирует определённую конструкцию SQL
            await RunDemoQueriesAsync();

            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();
        }

        /// <summary>
        /// Создаёт таблицу products (если не существует) и вставляет начальные строки.
        /// Все операции выполняются в рамках одного соединения.
        /// </summary>
        static async Task SetupDatabaseAsync()
        {
            // Открываем новое соединение с БД
            await using var conn = new NpgsqlConnection(connectionString);
            await conn.OpenAsync();

            // SQL-команда для создания таблицы, если её ещё нет
            string createTableSql = @"
                CREATE TABLE IF NOT EXISTS products (
                    id SERIAL PRIMARY KEY,          -- уникальный идентификатор, автоинкремент
                    name VARCHAR(100) NOT NULL,     -- название товара
                    category VARCHAR(50),           -- категория (может быть NULL)
                    price NUMERIC(10,2),            -- цена с двумя знаками после запятой
                    stock INT DEFAULT 0,            -- остаток на складе
                    description TEXT                -- описание (может быть NULL)
                );
            ";

            await using var cmdCreate = new NpgsqlCommand(createTableSql, conn);
            await cmdCreate.ExecuteNonQueryAsync();   // Выполняем DDL-команду (CREATE TABLE)

            // Проверяем, есть ли уже данные в таблице
            string checkSql = "SELECT COUNT(*) FROM products;";
            await using var cmdCheck = new NpgsqlCommand(checkSql, conn);
            long count = (long)(await cmdCheck.ExecuteScalarAsync())!;  // Получаем количество строк

            // Если таблица пуста – вставляем тестовые записи
            if (count == 0)
            {
                string insertSql = @"
                    INSERT INTO products (name, category, price, stock, description) VALUES
                    ('Ноутбук Pro', 'Электроника', 1200.00, 10, 'Мощный ноутбук для работы'),
                    ('Наушники Basic', 'Электроника', 50.00, 100, NULL),
                    ('Книга «SQL для всех»', 'Книги', 35.00, 5, 'Учебное пособие'),
                    ('Футболка Хлопок', 'Одежда', 15.00, 200, 'Удобная футболка'),
                    ('Смартфон Ultra', 'Электроника', 800.00, 0, 'Флагманский смартфон'),
                    ('Кофемашина', 'Бытовая техника', NULL, 3, 'Автоматическая кофемашина'),
                    ('Ручка гелевая', 'Канцелярия', 2.50, 0, NULL);
                ";
                await using var cmdInsert = new NpgsqlCommand(insertSql, conn);
                await cmdInsert.ExecuteNonQueryAsync();  // Вставляем сразу несколько строк
                Console.WriteLine("Тестовые данные добавлены в таблицу products.\n");
            }
            else
            {
                Console.WriteLine($"Таблица products уже содержит {count} записей. Пропускаем вставку.\n");
            }
        }

        /// <summary>
        /// Выполняет демонстрационные SQL-запросы и выводит результаты.
        /// Каждый запрос сопровождается поясняющим комментарием.
        /// </summary>
        static async Task RunDemoQueriesAsync()
        {
            // Создаём и открываем соединение
            await using var conn = new NpgsqlConnection(connectionString);
            await conn.OpenAsync();

            // ========================================================
            // 1. SELECT определённых колонок вместо *
            //    Получаем только название и цену всех товаров.
            // ========================================================
            string query1 = "SELECT name, price FROM products;";
            Console.WriteLine("1. SELECT конкретных колонок (name, price):");
            await ExecuteAndPrintAsync(conn, query1);

            // ========================================================
            // 2. WHERE с оператором = (равно)
            //    Товары из категории 'Электроника'.
            // ========================================================
            string query2 = "SELECT name, price FROM products WHERE category = 'Электроника';";
            Console.WriteLine("\n2. WHERE category = 'Электроника':");
            await ExecuteAndPrintAsync(conn, query2);

            // ========================================================
            // 3. WHERE с оператором > (больше)
            //    Товары с ценой больше 100.
            // ========================================================
            string query3 = "SELECT name, price FROM products WHERE price > 100;";
            Console.WriteLine("\n3. WHERE price > 100:");
            await ExecuteAndPrintAsync(conn, query3);

            // ========================================================
            // 4. WHERE с оператором < (меньше)
            //    Товары с остатком меньше 50.
            // ========================================================
            string query4 = "SELECT name, stock FROM products WHERE stock < 50;";
            Console.WriteLine("\n4. WHERE stock < 50:");
            await ExecuteAndPrintAsync(conn, query4);

            // ========================================================
            // 5. WHERE с IN (вхождение в список значений)
            //    Категории 'Книги' или 'Одежда'.
            // ========================================================
            string query5 = "SELECT name, category FROM products WHERE category IN ('Книги', 'Одежда');";
            Console.WriteLine("\n5. WHERE category IN ('Книги', 'Одежда'):");
            await ExecuteAndPrintAsync(conn, query5);

            // ========================================================
            // 6. WHERE с LIKE (поиск по шаблону)
            //    Название начинается с 'Ноутбук' (знак % означает любые символы).
            // ========================================================
            string query6 = "SELECT name, price FROM products WHERE name LIKE 'Ноутбук%';";
            Console.WriteLine("\n6. WHERE name LIKE 'Ноутбук%':");
            await ExecuteAndPrintAsync(conn, query6);

            // ========================================================
            // 7. WHERE с IS NULL (проверка на отсутствие значения)
            //    Товары, у которых нет описания.
            // ========================================================
            string query7 = "SELECT name, description FROM products WHERE description IS NULL;";
            Console.WriteLine("\n7. WHERE description IS NULL:");
            await ExecuteAndPrintAsync(conn, query7);

            // ========================================================
            // 8. Логический оператор AND
            //    Цена > 50 И остаток > 0.
            // ========================================================
            string query8 = "SELECT name, price, stock FROM products WHERE price > 50 AND stock > 0;";
            Console.WriteLine("\n8. WHERE price > 50 AND stock > 0:");
            await ExecuteAndPrintAsync(conn, query8);

            // ========================================================
            // 9. Логический оператор OR
            //    Категория 'Электроника' ИЛИ 'Книги'.
            // ========================================================
            string query9 = "SELECT name, category FROM products WHERE category = 'Электроника' OR category = 'Книги';";
            Console.WriteLine("\n9. WHERE category = 'Электроника' OR category = 'Книги':");
            await ExecuteAndPrintAsync(conn, query9);

            // ========================================================
            // 10. Логический оператор NOT
            //     Категория НЕ 'Одежда'.
            // ========================================================
            string query10 = "SELECT name, category FROM products WHERE NOT category = 'Одежда';";
            Console.WriteLine("\n10. WHERE NOT category = 'Одежда':");
            await ExecuteAndPrintAsync(conn, query10);

            // ========================================================
            // 11. ORDER BY – сортировка по цене по убыванию (DESC),
            //     а при равной цене – по названию по возрастанию (ASC).
            // ========================================================
            string query11 = "SELECT name, price FROM products ORDER BY price DESC, name ASC;";
            Console.WriteLine("\n11. ORDER BY price DESC, name ASC:");
            await ExecuteAndPrintAsync(conn, query11);

            // ========================================================
            // 12. Демонстрация SQL-комментариев прямо в запросе.
            //     В SQL можно использовать -- (однострочный) и /* */ (многострочный).
            //     Комментарии игнорируются сервером, запрос выполнится как обычно.
            // ========================================================
            string queryWithComments = @"
                -- Однострочный комментарий: выберем все товары с ценой больше 10
                SELECT name, price
                FROM products
                WHERE price > 10   /* многострочный комментарий
                                      начинается здесь
                                      и заканчивается */ 
                ORDER BY name;     -- сортировка по имени
            ";
            Console.WriteLine("\n12. Запрос с SQL-комментариями (-- и /* */):");
            Console.WriteLine("Текст запроса с комментариями:\n" + queryWithComments);
            await ExecuteAndPrintAsync(conn, queryWithComments);
        }

        /// <summary>
        /// Выполняет SQL-запрос, получает результат в DataTable
        /// и выводит его содержимое в консоль в виде простой таблицы.
        /// </summary>
        /// <param name="conn">Открытое соединение с БД</param>
        /// <param name="sql">SQL-запрос для выполнения</param>
        static async Task ExecuteAndPrintAsync(NpgsqlConnection conn, string sql)
        {
            // Создаём команду, связываем с соединением и задаём текст запроса
            await using var cmd = new NpgsqlCommand(sql, conn);

            // Объект для хранения данных, полученных из БД
            var dataTable = new DataTable();

            // Выполняем запрос асинхронно и загружаем результат в DataTable
            // NpgsqlDataReader читает данные построчно
            await using (var reader = await cmd.ExecuteReaderAsync())
            {
                // Заполняем DataTable схемой и строками из reader'а
                dataTable.Load(reader);
            }

            // Если данных нет – сообщаем об этом
            if (dataTable.Rows.Count == 0)
            {
                Console.WriteLine("   (нет результатов)");
                return;
            }

            // Вычисляем максимальную ширину каждой колонки для выравнивания
            int[] columnWidths = new int[dataTable.Columns.Count];
            for (int i = 0; i < dataTable.Columns.Count; i++)
            {
                // Начальная ширина – длина названия колонки
                columnWidths[i] = dataTable.Columns[i].ColumnName.Length;
            }
            foreach (DataRow row in dataTable.Rows)
            {
                for (int i = 0; i < dataTable.Columns.Count; i++)
                {
                    // Приводим значение к строке (для NULL выводим "NULL")
                    string val = row[i] is DBNull ? "NULL" : row[i].ToString()!;
                    if (val.Length > columnWidths[i])
                        columnWidths[i] = val.Length;
                }
            }

            // Выводим заголовки колонок
            for (int i = 0; i < dataTable.Columns.Count; i++)
            {
                Console.Write(dataTable.Columns[i].ColumnName.PadRight(columnWidths[i] + 2));
            }
            Console.WriteLine();

            // Выводим разделительную линию
            foreach (int w in columnWidths)
            {
                Console.Write(new string('-', w) + "  ");
            }
            Console.WriteLine();

            // Выводим строки данных
            foreach (DataRow row in dataTable.Rows)
            {
                for (int i = 0; i < dataTable.Columns.Count; i++)
                {
                    string val = row[i] is DBNull ? "NULL" : row[i].ToString()!;
                    Console.Write(val.PadRight(columnWidths[i] + 2));
                }
                Console.WriteLine();
            }
        }
    }
}