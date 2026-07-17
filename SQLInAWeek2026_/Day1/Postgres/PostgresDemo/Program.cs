using Npgsql;               // Пространство имён для работы с PostgreSQL
using System.Data;           // Для работы с интерфейсами IDbConnection и др.

namespace PostgresDemo;

class Program
{
    // Строка подключения к Postgres Pro (или обычному PostgreSQL).
    // Замените значения на свои: хост, порт, имя БД, пользователь, пароль.
    private const string ConnectionString =
        "Host=localhost;Port=5432;Database=testdb;Username=postgres;Password=Vozinja01234!";

    static async Task Main(string[] args)
    {
        // 1. Создаём объект подключения с использованием строки подключения.
        await using var connection = new NpgsqlConnection(ConnectionString);

        try
        {
            // 2. Открываем соединение с базой данных (асинхронно).
            await connection.OpenAsync();
            Console.WriteLine("✅ Подключение к Postgres Pro установлено.\n");

            // 3. Создаём таблицу Employees, если она ещё не существует.
            await CreateTableIfNotExists(connection);

            // 4. Вставляем несколько тестовых записей (если таблица пуста).
            await InsertSampleData(connection);

            // 5. Выполняем запрос SELECT * FROM Employees и выводим результат.
            await SelectAllEmployees(connection);
        }
        catch (Exception ex)
        {
            // Обработка ошибок подключения, выполнения запросов и т.п.
            Console.WriteLine($"❌ Ошибка: {ex.Message}");
        }
        finally
        {
            // 6. Соединение будет автоматически закрыто при выходе из using.
            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }

    /// <summary>
    /// Создаёт таблицу Employees, если она отсутствует.
    /// Демонстрирует основные типы данных SQL: serial, text, integer, date, numeric, boolean.
    /// </summary>
    private static async Task CreateTableIfNotExists(NpgsqlConnection connection)
    {
        // SQL-скрипт для создания таблицы.
        // - id: автоинкрементируемый первичный ключ (serial)
        // - full_name: текст (VARCHAR(100)) – строковые данные ограничены по длине
        // - age: целое число (INTEGER) – возраст
        // - hire_date: дата (DATE) – дата приёма на работу
        // - salary: число с плавающей точкой (NUMERIC(10,2)) – зарплата с двумя знаками после запятой
        // - is_active: булевый тип (BOOLEAN) – активен ли сотрудник
        // - department: текст (VARCHAR(50)) – отдел
        string createTableSql = @"
            CREATE TABLE IF NOT EXISTS Employees (
                id SERIAL PRIMARY KEY,
                full_name VARCHAR(100) NOT NULL,
                age INTEGER,
                hire_date DATE,
                salary NUMERIC(10, 2),
                is_active BOOLEAN DEFAULT true,
                department VARCHAR(50)
            );
        ";

        // Создаём команду с указанным SQL-запросом и подключением.
        await using var cmd = new NpgsqlCommand(createTableSql, connection);

        // Выполняем запрос, который не возвращает данные (ExecuteNonQuery).
        await cmd.ExecuteNonQueryAsync();

        Console.WriteLine("📋 Таблица Employees проверена / создана.");
    }

    /// <summary>
    /// Вставляет тестовые данные, если таблица пуста.
    /// </summary>
    private static async Task InsertSampleData(NpgsqlConnection connection)
    {
        // Проверяем, есть ли уже записи в таблице.
        string countSql = "SELECT COUNT(*) FROM Employees;";
        await using var countCmd = new NpgsqlCommand(countSql, connection);

        // ExecuteScalar возвращает первый столбец первой строки результата.
        long count = (long)(await countCmd.ExecuteScalarAsync() ?? 0L);

        if (count > 0)
        {
            Console.WriteLine($"📊 В таблице уже есть {count} записей. Пропускаем вставку.\n");
            return;
        }

        // SQL-запрос для вставки нескольких сотрудников.
        // Обратите внимание на использование параметров (параметризованные запросы) –
        // это защищает от SQL-инъекций и правильно обрабатывает типы.
        string insertSql = @"
            INSERT INTO Employees (full_name, age, hire_date, salary, is_active, department)
            VALUES 
                (@name1, @age1, @date1, @salary1, @active1, @dept1),
                (@name2, @age2, @date2, @salary2, @active2, @dept2),
                (@name3, @age3, @date3, @salary3, @active3, @dept3);
        ";

        await using var cmd = new NpgsqlCommand(insertSql, connection);

        // Добавляем параметры с указанием типов (NpgsqlDbType) – явное задание типа улучшает производительность и надёжность.
        // Первый сотрудник
        cmd.Parameters.AddWithValue("name1", "Иван Петров");
        cmd.Parameters.AddWithValue("age1", 30);
        cmd.Parameters.AddWithValue("date1", new DateOnly(2020, 5, 15));  // DateOnly для даты
        cmd.Parameters.AddWithValue("salary1", 75000.50m);
        cmd.Parameters.AddWithValue("active1", true);
        cmd.Parameters.AddWithValue("dept1", "IT");

        // Второй сотрудник
        cmd.Parameters.AddWithValue("name2", "Мария Смирнова");
        cmd.Parameters.AddWithValue("age2", 28);
        cmd.Parameters.AddWithValue("date2", new DateOnly(2021, 8, 22));
        cmd.Parameters.AddWithValue("salary2", 82000.00m);
        cmd.Parameters.AddWithValue("active2", true);
        cmd.Parameters.AddWithValue("dept2", "HR");

        // Третий сотрудник
        cmd.Parameters.AddWithValue("name3", "Алексей Кузнецов");
        cmd.Parameters.AddWithValue("age3", 45);
        cmd.Parameters.AddWithValue("date3", new DateOnly(2015, 3, 10));
        cmd.Parameters.AddWithValue("salary3", 120000.75m);
        cmd.Parameters.AddWithValue("active3", false);
        cmd.Parameters.AddWithValue("dept3", "Finance");

        // Выполняем вставку
        int rowsAffected = await cmd.ExecuteNonQueryAsync();
        Console.WriteLine($"✅ Добавлено {rowsAffected} записей в таблицу Employees.\n");
    }

    /// <summary>
    /// Выполняет SELECT * FROM Employees и выводит результат в виде таблицы.
    /// </summary>
    private static async Task SelectAllEmployees(NpgsqlConnection connection)
    {
        string selectSql = "SELECT * FROM Employees ORDER BY id;";
        await using var cmd = new NpgsqlCommand(selectSql, connection);

        // ExecuteReader возвращает объект для чтения набора данных.
        await using var reader = await cmd.ExecuteReaderAsync();

        // Проверяем, есть ли строки.
        if (!reader.HasRows)
        {
            Console.WriteLine("⚠️ Таблица Employees пуста.");
            return;
        }

        // Выводим заголовки столбцов с их типами (для демонстрации важности типов).
        Console.WriteLine("Результат SELECT * FROM Employees:");
        Console.WriteLine("------------------------------------------------------------");

        // Получаем схему (метаданные) результата.
        DataTable schemaTable = reader.GetSchemaTable();
        if (schemaTable != null)
        {
            // Печатаем имена столбцов и их типы данных (из схемы).
            Console.Write("| ");
            foreach (DataRow row in schemaTable.Rows)
            {
                string colName = row["ColumnName"].ToString()!;
                string dataType = row["DataTypeName"].ToString()!;
                Console.Write($"{colName} ({dataType}) | ");
            }
            Console.WriteLine();
            Console.WriteLine("------------------------------------------------------------");
        }

        // Читаем строки по одной.
        while (await reader.ReadAsync())
        {
            // Получаем значения по индексу или по имени столбца.
            int id = reader.GetInt32(0);                          // id (serial)
            string fullName = reader.GetString(1);                // full_name (varchar)
            int? age = reader.IsDBNull(2) ? null : reader.GetInt32(2); // age (integer)
            DateOnly? hireDate = reader.IsDBNull(3)
                ? null
                : DateOnly.FromDateTime(reader.GetDateTime(3));  // hire_date (date)
            decimal? salary = reader.IsDBNull(4)
                ? null
                : reader.GetDecimal(4);                           // salary (numeric)
            bool isActive = reader.GetBoolean(5);                 // is_active (boolean)
            string? department = reader.IsDBNull(6)
                ? null
                : reader.GetString(6);                            // department (varchar)

            // Выводим данные в читаемом формате.
            Console.Write($"| {id,-3} | {fullName,-20} | ");
            Console.Write($"{age?.ToString() ?? "NULL",-6} | ");
            Console.Write($"{hireDate?.ToString("yyyy-MM-dd") ?? "NULL",-12} | ");
            Console.Write($"{salary?.ToString("F2") ?? "NULL",-10} | ");
            Console.Write($"{isActive,-8} | ");
            Console.WriteLine($"{department ?? "NULL",-12} |");
        }

        Console.WriteLine("------------------------------------------------------------");
        Console.WriteLine("📌 Обратите внимание на типы данных:");
        Console.WriteLine("   - id (serial) – автоинкремент, целое число");
        Console.WriteLine("   - full_name (varchar) – текст с ограничением длины");
        Console.WriteLine("   - age (integer) – целое число, может быть NULL");
        Console.WriteLine("   - hire_date (date) – дата без времени");
        Console.WriteLine("   - salary (numeric) – точное десятичное число (деньги)");
        Console.WriteLine("   - is_active (boolean) – истина/ложь");
        Console.WriteLine("   - department (varchar) – текст, допускает NULL");
        Console.WriteLine("\n💡 Правильный выбор типа данных экономит место, повышает скорость запросов и защищает от ошибок.");
    }
}