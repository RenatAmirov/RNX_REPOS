namespace AggregationDemo
{
    using Npgsql; // Пространство имён для работы с PostgreSQL

    class Program
    {
        // Строка подключения к PostgreSQL (измените параметры под свою базу)
        private const string ConnectionString =
            "Host=localhost;Port=5432;Database=testdb;Username=postgres;Password=Vozinja01234!";

        static async Task Main(string[] args)
        {
            // Создаём соединение с базой данных
            await using var connection = new NpgsqlConnection(ConnectionString);

            try
            {
                // Открываем соединение
                await connection.OpenAsync();
                Console.WriteLine("Соединение с PostgreSQL установлено.\n");

                // Шаг 1: создание таблицы, если её ещё нет
                await CreateTableIfNotExists(connection);

                // Шаг 2: заполнение таблицы демонстрационными данными (если она пуста)
                await InsertSampleDataIfEmpty(connection);

                // Шаг 3: выполнение агрегационных запросов с подробными пояснениями
                await DemonstrateAggregations(connection);
            }
            catch (Exception ex)
            {
                // Выводим ошибку, если что-то пошло не так
                Console.WriteLine($"Ошибка: {ex.Message}");
            }
        }

        // Метод создания таблицы сотрудников
        private static async Task CreateTableIfNotExists(NpgsqlConnection connection)
        {
            // SQL-запрос на создание таблицы, если она не существует
            const string createTableSql = @"
            CREATE TABLE IF NOT EXISTS Employees (
                Id SERIAL PRIMARY KEY,          -- Уникальный идентификатор
                Name VARCHAR(100) NOT NULL,     -- Имя сотрудника
                Department VARCHAR(50) NOT NULL,-- Отдел
                Salary NUMERIC(10,2) NOT NULL   -- Зарплата (число с двумя знаками после запятой)
            );
        ";

            // Создаём команду для выполнения SQL-запроса
            await using var cmd = new NpgsqlCommand(createTableSql, connection);

            // Выполняем запрос (ничего не возвращает, просто создаёт таблицу)
            await cmd.ExecuteNonQueryAsync();
            Console.WriteLine("Таблица Employees готова к работе.");
        }

        // Метод вставки тестовых данных, если таблица пуста
        private static async Task InsertSampleDataIfEmpty(NpgsqlConnection connection)
        {
            // Проверяем, есть ли записи в таблице
            const string checkSql = "SELECT COUNT(*) FROM Employees;";
            await using var checkCmd = new NpgsqlCommand(checkSql, connection);

            // Выполняем запрос и получаем скалярное значение (количество записей)
            var count = (long)(await checkCmd.ExecuteScalarAsync())!;

            if (count > 0)
            {
                Console.WriteLine("Таблица уже содержит данные. Пропускаем вставку.\n");
                return;
            }

            // Данные для вставки: имя, отдел, зарплата
            var employees = new[]
            {
            ("Иван Петров",   "IT",       75000m),
            ("Мария Смирнова","IT",       82000m),
            ("Пётр Сидоров",  "IT",       68000m),
            ("Анна Иванова",  "HR",       60000m),
            ("Олег Фёдоров",  "HR",       63000m),
            ("Светлана Козлова","HR",     59000m),
            ("Дмитрий Орлов", "Sales",    72000m),
            ("Елена Воробьёва","Sales",   69000m),
            ("Алексей Гусев", "Sales",    71000m),
            ("Ольга Медведева","Sales",   68000m),
            ("Николай Зайцев","Sales",    55000m), // Низкая зарплата для демонстрации HAVING
        };

            // SQL-запрос вставки с параметрами для безопасности и производительности
            const string insertSql = @"
            INSERT INTO Employees (Name, Department, Salary)
            VALUES (@name, @department, @salary);
        ";

            // Создаём команду один раз и будем менять параметры в цикле
            await using var insertCmd = new NpgsqlCommand(insertSql, connection);

            // Определяем параметры команды
            var nameParam = insertCmd.Parameters.Add("@name", NpgsqlTypes.NpgsqlDbType.Varchar);
            var deptParam = insertCmd.Parameters.Add("@department", NpgsqlTypes.NpgsqlDbType.Varchar);
            var salaryParam = insertCmd.Parameters.Add("@salary", NpgsqlTypes.NpgsqlDbType.Numeric);

            // Вставляем каждую запись
            foreach (var (name, dept, salary) in employees)
            {
                nameParam.Value = name;
                deptParam.Value = dept;
                salaryParam.Value = salary;

                await insertCmd.ExecuteNonQueryAsync();
            }

            Console.WriteLine($"Вставлено {employees.Length} записей.\n");
        }

        // Метод, демонстрирующий все необходимые агрегатные запросы
        private static async Task DemonstrateAggregations(NpgsqlConnection connection)
        {
            // ----- 1. Простой COUNT -----
            // Считаем общее количество сотрудников
            Console.WriteLine("=== COUNT (общее количество сотрудников) ===");
            const string totalCountSql = "SELECT COUNT(*) FROM Employees;";
            await using var countCmd = new NpgsqlCommand(totalCountSql, connection);
            var total = (long)(await countCmd.ExecuteScalarAsync())!;
            Console.WriteLine($"Всего сотрудников: {total}\n");

            // ----- 2. COUNT с GROUP BY -----
            // Считаем количество сотрудников в каждом отделе
            Console.WriteLine("=== COUNT + GROUP BY (количество по отделам) ===");
            const string countByDeptSql = @"
            SELECT Department, COUNT(*) AS EmployeeCount
            FROM Employees
            GROUP BY Department
            ORDER BY EmployeeCount DESC;
        ";
            await using var countByDeptCmd = new NpgsqlCommand(countByDeptSql, connection);
            await using var countReader = await countByDeptCmd.ExecuteReaderAsync();

            while (await countReader.ReadAsync())
            {
                string dept = countReader.GetString(0);
                long empCount = countReader.GetInt64(1);
                Console.WriteLine($"Отдел {dept}: {empCount} чел.");
            }
            Console.WriteLine();

            // ----- 3. SUM, AVG, MIN, MAX с GROUP BY -----
            // Вычисляем суммарную, среднюю, минимальную и максимальную зарплату по отделам
            Console.WriteLine("=== SUM, AVG, MIN, MAX + GROUP BY (зарплаты по отделам) ===");
            const string statsByDeptSql = @"
            SELECT 
                Department,
                SUM(Salary)   AS TotalSalary,   -- Сумма зарплат
                AVG(Salary)   AS AvgSalary,     -- Средняя зарплата
                MIN(Salary)   AS MinSalary,     -- Минимальная зарплата
                MAX(Salary)   AS MaxSalary      -- Максимальная зарплата
            FROM Employees
            GROUP BY Department
            ORDER BY Department;
        ";
            await using var statsCmd = new NpgsqlCommand(statsByDeptSql, connection);
            await using var statsReader = await statsCmd.ExecuteReaderAsync();

            Console.WriteLine($"{"Отдел",-10} {"Сумма",-12} {"Средняя",-10} {"Мин.",-10} {"Макс.",-10}");
            while (await statsReader.ReadAsync())
            {
                string dept = statsReader.GetString(0);
                decimal totalSal = statsReader.GetDecimal(1);
                double avgSal = statsReader.GetDouble(2);  // AVG возвращает double
                decimal minSal = statsReader.GetDecimal(3);
                decimal maxSal = statsReader.GetDecimal(4);

                Console.WriteLine(
                    $"{dept,-10} {totalSal,10:F2} {avgSal,10:F2} {minSal,10:F2} {maxSal,10:F2}");
            }
            Console.WriteLine();

            // ----- 4. HAVING – фильтрация сгруппированных данных -----
            // Показываем только те отделы, где средняя зарплата > 65000
            Console.WriteLine("=== HAVING (отделы со средней зарплатой > 65000) ===");
            const string havingSql = @"
            SELECT 
                Department,
                AVG(Salary) AS AvgSalary
            FROM Employees
            GROUP BY Department
            HAVING AVG(Salary) > 65000   -- Условие применяется после группировки
            ORDER BY AvgSalary DESC;
        ";
            await using var havingCmd = new NpgsqlCommand(havingSql, connection);
            await using var havingReader = await havingCmd.ExecuteReaderAsync();

            Console.WriteLine($"{"Отдел",-10} {"Средняя з/п",-12}");
            while (await havingReader.ReadAsync())
            {
                string dept = havingReader.GetString(0);
                double avgSal = havingReader.GetDouble(1);
                Console.WriteLine($"{dept,-10} {avgSal,10:F2}");
            }
            Console.WriteLine();

            // ----- 5. Демонстрация разницы WHERE и HAVING -----
            // WHERE фильтрует строки ДО группировки, HAVING – ПОСЛЕ.
            // Например: найдём среднюю зарплату в отделах, исключая сотрудников с зарплатой < 60000,
            // и покажем только те отделы, где эта средняя больше 70000.

            Console.WriteLine("=== WHERE + HAVING (сначала исключаем низкие зарплаты, затем фильтруем среднюю) ===");
            const string whereHavingSql = @"
            SELECT 
                Department,
                AVG(Salary) AS FilteredAvg
            FROM Employees
            WHERE Salary >= 60000         -- фильтруем строки ДО группировки
            GROUP BY Department
            HAVING AVG(Salary) > 70000    -- фильтруем группы ПОСЛЕ вычисления среднего
            ORDER BY FilteredAvg DESC;
        ";
            await using var whCmd = new NpgsqlCommand(whereHavingSql, connection);
            await using var whReader = await whCmd.ExecuteReaderAsync();

            Console.WriteLine($"{"Отдел",-10} {"Средняя (после фильтров)",-25}");
            while (await whReader.ReadAsync())
            {
                string dept = whReader.GetString(0);
                double avgSal = whReader.GetDouble(1);
                Console.WriteLine($"{dept,-10} {avgSal,10:F2}");
            }
            Console.WriteLine();

            Console.WriteLine("Демонстрация завершена. Нажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}
