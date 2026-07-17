namespace JoinDemo
{
    // =============================================================================
    // Проект: Демонстрация JOIN-запросов в PostgreSQL с использованием C# и Npgsql
    // Тема:  "День 3 (Вторник) — соединения таблиц (JOIN)"
    // 
    // Для запуска необходимо:
    // 1. Установить пакет Npgsql через NuGet: dotnet add package Npgsql
    // 2. Настроить строку подключения (см. переменную connectionString ниже)
    //    под свою установку PostgreSQL (хост, пользователь, пароль, имя БД).
    // 3. Убедиться, что база данных "joindemo" создана в PostgreSQL.
    // =============================================================================

    using System;                         // Базовые типы и консольный ввод/вывод
    using Npgsql;                         // Провайдер для работы с PostgreSQL из .NET

    class Program
    {
        // -------------------------------------------------------------------------
        // Точка входа в приложение
        // -------------------------------------------------------------------------
        static void Main()
        {
            // ---------- Строка подключения ----------
            // Замените параметры (Host, Username, Password, Database) на свои.
            string connectionString =
                "Host=localhost;" +                // адрес сервера PostgreSQL
                "Username=postgres;" +            // имя пользователя
                "Password=Vozinja01234!;" +        // пароль пользователя
                "Database=testdb";              // имя базы данных (должна существовать)

            // Создаём объект подключения. using гарантирует автоматический вызов Dispose(),
            // который закроет соединение даже при возникновении ошибок.
            using var conn = new NpgsqlConnection(connectionString);

            try
            {
                conn.Open();                     // Открываем физическое соединение с СУБД

                // Последовательный вызов методов, решающих задачу
                CreateTables(conn);              // Создаём таблицы, если их ещё нет
                InsertSampleData(conn);          // Наполняем таблицы тестовыми данными
                RunJoinQueries(conn);            // Выполняем и выводим результаты всех JOIN

                Console.WriteLine("\nГотово. Все запросы выполнены успешно.");
            }
            catch (Exception ex)
            {
                // Если на любом этапе возникла ошибка, выводим её описание
                Console.WriteLine($"Ошибка: {ex.Message}");
            }
            // Соединение закроется автоматически при выходе из блока using
        }

        // -------------------------------------------------------------------------
        // Создание таблиц Students, Courses и Enrollments,
        // если они ещё не существуют в базе данных.
        // -------------------------------------------------------------------------
        static void CreateTables(NpgsqlConnection conn)
        {
            // Многострочный SQL-скрипт, который безопасно создаёт таблицы.
            // IF NOT EXISTS предотвращает ошибку при повторном запуске.
            const string createTablesSql = @"
            CREATE TABLE IF NOT EXISTS Students (
                Id SERIAL PRIMARY KEY,        -- суррогатный ключ, автоинкремент
                Name VARCHAR(100) NOT NULL    -- имя студента
            );

            CREATE TABLE IF NOT EXISTS Courses (
                Id SERIAL PRIMARY KEY,        -- ключ курса
                Title VARCHAR(100) NOT NULL   -- название курса
            );

            CREATE TABLE IF NOT EXISTS Enrollments (
                StudentId INT REFERENCES Students(Id),   -- внешний ключ на студента
                CourseId INT REFERENCES Courses(Id),     -- внешний ключ на курс
                EnrollmentDate DATE NOT NULL,            -- дата записи
                PRIMARY KEY (StudentId, CourseId)        -- составной первичный ключ
            );

            -- Индексы для ускорения JOIN по внешним ключам (одна из тем «Производительность»)
            CREATE INDEX IF NOT EXISTS idx_enroll_student ON Enrollments(StudentId);
            CREATE INDEX IF NOT EXISTS idx_enroll_course  ON Enrollments(CourseId);
        ";

            // Создаём команду, передавая ей текст запроса и открытое соединение
            using var cmd = new NpgsqlCommand(createTablesSql, conn);
            cmd.ExecuteNonQuery();                // Выполняем DDL-команду без возврата данных
            Console.WriteLine("Таблицы созданы (или уже существовали).");
        }

        // -------------------------------------------------------------------------
        // Вставка небольшого набора тестовых данных для иллюстрации всех видов JOIN
        // -------------------------------------------------------------------------
        static void InsertSampleData(NpgsqlConnection conn)
        {
            // Очищаем таблицы, чтобы при повторном запуске данные не дублировались.
            // Порядок важен: сначала удаляем зависимые записи (Enrollments), потом основные.
            using (var cmd = new NpgsqlCommand("DELETE FROM Enrollments", conn))
                cmd.ExecuteNonQuery();
            using (var cmd = new NpgsqlCommand("DELETE FROM Students", conn))
                cmd.ExecuteNonQuery();
            using (var cmd = new NpgsqlCommand("DELETE FROM Courses", conn))
                cmd.ExecuteNonQuery();

            // Вставка студентов (4 записи)
            using (var cmd = new NpgsqlCommand())
            {
                cmd.Connection = conn;
                cmd.CommandText = "INSERT INTO Students (Name) VALUES (@name)";
                var nameParam = cmd.Parameters.Add("@name", NpgsqlTypes.NpgsqlDbType.Varchar);

                // Добавляем каждого студента отдельным вызовом ExecuteNonQuery
                nameParam.Value = "Анна"; cmd.ExecuteNonQuery();
                nameParam.Value = "Борис"; cmd.ExecuteNonQuery();
                nameParam.Value = "Виктор"; cmd.ExecuteNonQuery();
                nameParam.Value = "Галина"; cmd.ExecuteNonQuery(); // Этот студент не будет записан ни на один курс
            }

            // Вставка курсов (3 записи)
            using (var cmd = new NpgsqlCommand())
            {
                cmd.Connection = conn;
                cmd.CommandText = "INSERT INTO Courses (Title) VALUES (@title)";
                var titleParam = cmd.Parameters.Add("@title", NpgsqlTypes.NpgsqlDbType.Varchar);

                titleParam.Value = "Математика"; cmd.ExecuteNonQuery();
                titleParam.Value = "Физика"; cmd.ExecuteNonQuery();
                titleParam.Value = "Программирование"; cmd.ExecuteNonQuery(); // На этот курс пока никто не записан
            }

            // Вставка записей о зачислении (Enrollments) – некоторые студенты записаны на курсы
            using (var cmd = new NpgsqlCommand())
            {
                cmd.Connection = conn;
                cmd.CommandText = @"
                INSERT INTO Enrollments (StudentId, CourseId, EnrollmentDate)
                VALUES (@studentId, @courseId, @date)";
                var sParam = cmd.Parameters.Add("@studentId", NpgsqlTypes.NpgsqlDbType.Integer);
                var cParam = cmd.Parameters.Add("@courseId", NpgsqlTypes.NpgsqlDbType.Integer);
                var dParam = cmd.Parameters.Add("@date", NpgsqlTypes.NpgsqlDbType.Date);

                // Анна -> Математика и Физика
                sParam.Value = 1; cParam.Value = 1; dParam.Value = new DateTime(2026, 7, 1); cmd.ExecuteNonQuery();
                sParam.Value = 1; cParam.Value = 2; dParam.Value = new DateTime(2026, 7, 2); cmd.ExecuteNonQuery();

                // Борис -> Математика
                sParam.Value = 2; cParam.Value = 1; dParam.Value = new DateTime(2026, 7, 3); cmd.ExecuteNonQuery();

                // Виктор -> Физика
                sParam.Value = 3; cParam.Value = 2; dParam.Value = new DateTime(2026, 7, 4); cmd.ExecuteNonQuery();

                // Галина никуда не записана, курс "Программирование" пуст – специально для демонстрации OUTER JOIN.
            }

            Console.WriteLine("Тестовые данные вставлены.");
        }

        // -------------------------------------------------------------------------
        // Выполнение и вывод различных типов JOIN-запросов с пояснениями
        // -------------------------------------------------------------------------
        static void RunJoinQueries(NpgsqlConnection conn)
        {
            // ===================== 1. INNER JOIN =====================
            Console.WriteLine("\n=== INNER JOIN ===");
            Console.WriteLine("Только студенты, записанные хотя бы на один курс:");
            const string innerJoinSql = @"
            SELECT s.Name AS Student, c.Title AS Course
            FROM Students s
            INNER JOIN Enrollments e ON s.Id = e.StudentId   -- только совпадающие записи
            INNER JOIN Courses c     ON e.CourseId = c.Id
            ORDER BY s.Name, c.Title";
            ExecuteAndPrint(conn, innerJoinSql);

            // ===================== 2. LEFT JOIN =====================
            Console.WriteLine("\n=== LEFT JOIN ===");
            Console.WriteLine("Все студенты, даже не записанные на курсы (курс = NULL):");
            const string leftJoinSql = @"
            SELECT s.Name AS Student, c.Title AS Course
            FROM Students s
            LEFT JOIN Enrollments e ON s.Id = e.StudentId   -- все строки из Students
            LEFT JOIN Courses c     ON e.CourseId = c.Id
            ORDER BY s.Name, c.Title";
            ExecuteAndPrint(conn, leftJoinSql);

            // ===================== 3. RIGHT JOIN =====================
            Console.WriteLine("\n=== RIGHT JOIN ===");
            Console.WriteLine("Все курсы, даже те, на которые никто не записан (студент = NULL):");
            // Демонстрируем RIGHT JOIN, присоединяя Enrollments и Students к таблице Courses.
            const string rightJoinSql = @"
            SELECT c.Title AS Course, s.Name AS Student
            FROM Courses c
            LEFT JOIN Enrollments e ON c.Id = e.CourseId
            LEFT JOIN Students s     ON e.StudentId = s.Id
            ORDER BY c.Title, s.Name";
            Console.WriteLine("(Аналог RIGHT JOIN: Courses LEFT JOIN ...)");
            ExecuteAndPrint(conn, rightJoinSql);

            // Для явного RIGHT JOIN можно перевернуть порядок таблиц, но логика та же.
            // Покажем ещё один вариант с RIGHT JOIN в стиле PostgreSQL:
            const string explicitRightJoinSql = @"
            SELECT s.Name AS Student, c.Title AS Course
            FROM Enrollments e
            RIGHT JOIN Students s ON e.StudentId = s.Id
            RIGHT JOIN Courses c   ON e.CourseId = c.Id
            ORDER BY c.Title, s.Name";
            Console.WriteLine("Явный RIGHT JOIN (Students и Courses справа от Enrollments):");
            ExecuteAndPrint(conn, explicitRightJoinSql);

            // ===================== 4. FULL OUTER JOIN =====================
            Console.WriteLine("\n=== FULL OUTER JOIN ===");
            Console.WriteLine("Абсолютно все записи: студенты без курсов и курсы без студентов:");
            // В PostgreSQL FULL OUTER JOIN выполняется напрямую.
            // Объединяем Students и Enrollments, затем Courses, чтобы увидеть полную картину.
            const string fullOuterSql = @"
            SELECT s.Name AS Student, c.Title AS Course
            FROM Students s
            FULL OUTER JOIN Enrollments e ON s.Id = e.StudentId
            FULL OUTER JOIN Courses c      ON e.CourseId = c.Id
            ORDER BY s.Name, c.Title";
            ExecuteAndPrint(conn, fullOuterSql);

            // ===================== 5. Производительность =====================
            Console.WriteLine("\n=== Советы по производительности ===");
            Console.WriteLine("1. Индексы на внешних ключах (уже созданы) ускоряют JOIN.");
            Console.WriteLine("2. Избегайте SELECT * – выбирайте только нужные столбцы.");
            Console.WriteLine("3. Используйте INNER JOIN вместо OUTER, если NULL-значения не нужны.");
            Console.WriteLine("   (INNER JOIN может выполняться быстрее, т.к. отсекает строки без совпадений.)");

            // Пример запроса, который выбирает только нужные поля (не *).
            const string selectSpecificColumns = @"
            SELECT s.Name, c.Title   -- только два столбца вместо *
            FROM Students s
            INNER JOIN Enrollments e ON s.Id = e.StudentId
            INNER JOIN Courses c     ON e.CourseId = c.Id
            ORDER BY s.Name, c.Title";
            Console.WriteLine("\nПример с выбором конкретных столбцов (не SELECT *):");
            ExecuteAndPrint(conn, selectSpecificColumns);
        }

        // -------------------------------------------------------------------------
        // Вспомогательный метод: выполняет переданный SELECT-запрос и выводит
        // результат в консоль в виде таблицы.
        // -------------------------------------------------------------------------
        static void ExecuteAndPrint(NpgsqlConnection conn, string sql)
        {
            using var cmd = new NpgsqlCommand(sql, conn);   // создаём команду
            using var reader = cmd.ExecuteReader();         // выполняем запрос и получаем reader

            // Выводим названия столбцов как заголовок
            for (int i = 0; i < reader.FieldCount; i++)
            {
                Console.Write($"{reader.GetName(i),-20}"); // каждый заголовок занимает 20 символов, выравнивание влево
            }
            Console.WriteLine();

            // Читаем построчно
            while (reader.Read())
            {
                for (int i = 0; i < reader.FieldCount; i++)
                {
                    // Получаем значение ячейки, NULL отображаем как "NULL"
                    object value = reader.IsDBNull(i) ? "NULL" : reader.GetValue(i);
                    Console.Write($"{value,-20}");
                }
                Console.WriteLine();
            }
            // reader автоматически закроется при выходе из using
        }
    }
}
