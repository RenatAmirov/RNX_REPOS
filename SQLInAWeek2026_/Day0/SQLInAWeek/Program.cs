using System;
using System.Data;
using System.Data.SQLite;
using System.Text;

namespace SQLInAWeek
{
    class Program
    {
        // Строка подключения к SQLite (файл базы данных будет создан в папке приложения)
        private static readonly string connectionString = "Data Source=DataNova.db;Version=3;";

        static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.UTF8; // Для корректного отображения символов

            Console.WriteLine("=== SQL in a Week — Демонстрационное приложение ===\n");

            // 1. Инициализация базы данных: создание таблиц и заполнение данными
            InitializeDatabase();

            // 2. Выполнение примеров запросов из книги
            RunQueries();

            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();
        }

        /// <summary>
        /// Создаёт базу данных и таблицы, если они ещё не существуют,
        /// и заполняет их тестовыми данными.
        /// </summary>
        static void InitializeDatabase()
        {
            using (var connection = new SQLiteConnection(connectionString))
            {
                connection.Open();

                // Проверяем, есть ли уже таблица Employees (признак того, что БД инициализирована)
                using (var cmd = new SQLiteCommand(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name='Employees';", connection))
                {
                    var result = cmd.ExecuteScalar();
                    if (result != null && result.ToString() == "Employees")
                    {
                        Console.WriteLine("База данных уже инициализирована. Пропускаем создание таблиц.\n");
                        return; // Данные уже есть
                    }
                }

                Console.WriteLine("Создание таблиц и заполнение тестовыми данными...");

                // ---- Создание таблиц ----
                // Таблица Departments
                string createDepartments = @"
                    CREATE TABLE IF NOT EXISTS Departments (
                        DepartmentID INTEGER PRIMARY KEY,
                        DepartmentName TEXT,
                        Manager TEXT
                    );";

                // Таблица Employees (ссылается на Departments)
                string createEmployees = @"
                    CREATE TABLE IF NOT EXISTS Employees (
                        EmployeeID INTEGER PRIMARY KEY,
                        FirstName TEXT,
                        LastName TEXT,
                        DepartmentID INTEGER,
                        Salary REAL,
                        Location TEXT,
                        HireDate TEXT,
                        FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
                    );";

                // Таблица Projects (ссылается на Departments)
                string createProjects = @"
                    CREATE TABLE IF NOT EXISTS Projects (
                        ProjectID INTEGER PRIMARY KEY,
                        ProjectName TEXT,
                        DepartmentID INTEGER,
                        Budget REAL,
                        StartDate TEXT,
                        FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
                    );";

                // Таблица Assignments (связь многие-ко-многим)
                string createAssignments = @"
                    CREATE TABLE IF NOT EXISTS Assignments (
                        EmployeeID INTEGER,
                        ProjectID INTEGER,
                        Role TEXT,
                        HoursPerWeek INTEGER,
                        PRIMARY KEY (EmployeeID, ProjectID),
                        FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
                        FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
                    );";

                // Таблица Timesheets
                string createTimesheets = @"
                    CREATE TABLE IF NOT EXISTS Timesheets (
                        EmployeeID INTEGER NOT NULL,
                        ProjectID INTEGER NOT NULL,
                        WeekStart TEXT NOT NULL,
                        Hours REAL NOT NULL,
                        FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
                    );";

                // Таблица SalaryChanges
                string createSalaryChanges = @"
                    CREATE TABLE IF NOT EXISTS SalaryChanges (
                        EmployeeID INTEGER NOT NULL,
                        EffectiveDate TEXT NOT NULL,
                        NewSalary REAL NOT NULL,
                        FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
                    );";

                // Выполняем создание каждой таблицы
                ExecuteNonQuery(connection, createDepartments);
                ExecuteNonQuery(connection, createEmployees);
                ExecuteNonQuery(connection, createProjects);
                ExecuteNonQuery(connection, createAssignments);
                ExecuteNonQuery(connection, createTimesheets);
                ExecuteNonQuery(connection, createSalaryChanges);

                // ---- Вставка данных ----
                // Departments
                string insertDepartments = @"
                    INSERT INTO Departments (DepartmentID, DepartmentName, Manager) VALUES
                    (1, 'Marketing', 'Laura Diaz'),
                    (2, 'Engineering', 'Sam Patel'),
                    (3, 'HR', 'Tina Chen'),
                    (4, 'Support', 'Rajiv Nair');";
                ExecuteNonQuery(connection, insertDepartments);

                // Employees
                string insertEmployees = @"
                    INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID, Salary, Location, HireDate) VALUES
                    (1, 'Alice', 'Johnson', 1, 72000.00, 'New York', '2021-04-01'),
                    (2, 'Bob', 'Lee', 2, 95000.00, 'San Francisco', '2020-01-15'),
                    (3, 'Carlos', 'Ramirez', 3, 65000.00, 'London', '2019-09-30'),
                    (4, 'Diana', 'Wang', 4, 60000.00, 'Bangalore', '2022-06-10'),
                    (5, 'Ethan', 'Kim', 2, 98000.00, 'Seoul', '2018-11-12'),
                    (6, 'Fiona', 'Davis', 1, 71000.00, 'New York', '2022-02-01'),
                    (7, 'George', 'Clark', 2, 105000.00, 'San Francisco', '2017-03-20'),
                    (8, 'Hannah', 'Zhang', 3, 67000.00, 'London', '2020-07-18'),
                    (9, 'Ivan', 'Petrov', 4, 59000.00, 'Bangalore', '2021-10-25'),
                    (10, 'Jenny', 'Nguyen', 2, 97000.00, 'Tokyo', '2019-12-03');";
                ExecuteNonQuery(connection, insertEmployees);

                // Projects
                string insertProjects = @"
                    INSERT INTO Projects (ProjectID, ProjectName, DepartmentID, Budget, StartDate) VALUES
                    (101, 'Brand Redesign', 1, 150000.00, '2023-01-01'),
                    (102, 'AI Chatbot', 2, 300000.00, '2022-07-15'),
                    (103, 'Recruitment Drive', 3, 80000.00, '2022-11-20'),
                    (104, 'Helpdesk Upgrade', 4, 60000.00, '2023-04-10'),
                    (105, 'Product Launch', 1, 200000.00, '2023-05-01'),
                    (106, 'Cloud Migration', 2, 400000.00, '2021-09-10'),
                    (107, 'Employee Onboarding', 3, 95000.00, '2022-03-15'),
                    (108, 'Ticket System Revamp', 4, 75000.00, '2023-06-01');";
                ExecuteNonQuery(connection, insertProjects);

                // Assignments
                string insertAssignments = @"
                    INSERT INTO Assignments (EmployeeID, ProjectID, Role, HoursPerWeek) VALUES
                    (1, 101, 'Coordinator', 10),
                    (2, 102, 'Developer', 20),
                    (3, 103, 'HR Lead', 15),
                    (4, 104, 'Support Agent', 25),
                    (5, 102, 'AI Engineer', 30),
                    (6, 105, 'Marketing Analyst', 12),
                    (7, 106, 'Cloud Architect', 25),
                    (8, 107, 'Trainer', 18),
                    (9, 108, 'IT Support', 20),
                    (10, 106, 'DevOps Engineer', 28),
                    (1, 105, 'Content Creator', 10),
                    (2, 106, 'Lead Engineer', 15);";
                ExecuteNonQuery(connection, insertAssignments);

                // Timesheets
                string insertTimesheets = @"
                    INSERT INTO Timesheets (EmployeeID, ProjectID, WeekStart, Hours) VALUES
                    (1, 101, '2023-06-05', 10),
                    (1, 105, '2023-06-05', 12),
                    (2, 102, '2023-06-05', 18),
                    (2, 106, '2023-06-05', 15),
                    (5, 102, '2023-06-05', 30),
                    (7, 106, '2023-06-05', 22),
                    (10, 106, '2023-06-05', 25),
                    (9, 108, '2023-06-05', 20),
                    (1, 101, '2023-06-12', 8),
                    (1, 105, '2023-06-12', 10),
                    (2, 102, '2023-06-12', 20),
                    (2, 106, '2023-06-12', 12),
                    (5, 102, '2023-06-12', 28),
                    (7, 106, '2023-06-12', 25),
                    (10, 106, '2023-06-12', 28),
                    (9, 108, '2023-06-12', 18);";
                ExecuteNonQuery(connection, insertTimesheets);

                // SalaryChanges
                string insertSalaryChanges = @"
                    INSERT INTO SalaryChanges (EmployeeID, EffectiveDate, NewSalary) VALUES
                    (1, '2022-01-01', 68000.00),
                    (1, '2023-04-01', 72000.00),
                    (2, '2020-01-15', 90000.00),
                    (2, '2022-08-01', 95000.00),
                    (5, '2019-11-12', 92000.00),
                    (5, '2022-05-01', 98000.00),
                    (7, '2018-01-01', 99000.00),
                    (7, '2021-03-01', 105000.00);";
                ExecuteNonQuery(connection, insertSalaryChanges);

                Console.WriteLine("База данных успешно инициализирована.\n");
            }
        }

        /// <summary>
        /// Вспомогательный метод для выполнения SQL-команд, не возвращающих результат.
        /// </summary>
        static void ExecuteNonQuery(SQLiteConnection connection, string sql)
        {
            using (var cmd = new SQLiteCommand(sql, connection))
            {
                cmd.ExecuteNonQuery();
            }
        }

        /// <summary>
        /// Выполняет SELECT-запрос и возвращает результат в виде DataTable.
        /// </summary>
        static DataTable ExecuteQuery(SQLiteConnection connection, string sql)
        {
            var dataTable = new DataTable();
            using (var cmd = new SQLiteCommand(sql, connection))
            using (var adapter = new SQLiteDataAdapter(cmd))
            {
                adapter.Fill(dataTable);
            }
            return dataTable;
        }

        /// <summary>
        /// Выводит содержимое DataTable в консоль в виде таблицы.
        /// </summary>
        static void PrintDataTable(DataTable table, string title = "")
        {
            if (!string.IsNullOrEmpty(title))
            {
                Console.WriteLine($"{title}:");
            }

            if (table.Rows.Count == 0)
            {
                Console.WriteLine("  (нет данных)");
                Console.WriteLine();
                return;
            }

            // Печатаем заголовки столбцов
            foreach (DataColumn col in table.Columns)
            {
                Console.Write(col.ColumnName.PadRight(20));
            }
            Console.WriteLine();

            // Разделительная линия
            for (int i = 0; i < table.Columns.Count; i++)
                Console.Write("".PadRight(20, '-'));
            Console.WriteLine();

            // Печатаем строки данных
            foreach (DataRow row in table.Rows)
            {
                foreach (DataColumn col in table.Columns)
                {
                    string value = row[col]?.ToString() ?? "NULL";
                    Console.Write(value.PadRight(20));
                }
                Console.WriteLine();
            }

            Console.WriteLine($"Количество строк: {table.Rows.Count}\n");
        }

        /// <summary>
        /// Запускает последовательное выполнение демонстрационных SQL-запросов из книги.
        /// </summary>
        static void RunQueries()
        {
            using (var connection = new SQLiteConnection(connectionString))
            {
                connection.Open();
                Console.WriteLine("=== Выполнение демонстрационных запросов ===\n");

                // 1. Простой SELECT (глава 1)
                string sql1 = "SELECT * FROM Employees;";
                DataTable dt1 = ExecuteQuery(connection, sql1);
                PrintDataTable(dt1, "1) Все сотрудники (SELECT *)");

                // 2. SELECT с фильтром WHERE (глава 2)
                string sql2 = "SELECT FirstName, LastName FROM Employees WHERE DepartmentID = 1;";
                DataTable dt2 = ExecuteQuery(connection, sql2);
                PrintDataTable(dt2, "2) Сотрудники отдела Marketing (DepartmentID=1)");

                // 3. Сортировка ORDER BY (глава 2)
                string sql3 = "SELECT FirstName, Salary FROM Employees ORDER BY Salary DESC;";
                DataTable dt3 = ExecuteQuery(connection, sql3);
                PrintDataTable(dt3, "3) Сотрудники по убыванию зарплаты");

                // 4. INNER JOIN (глава 3)
                string sql4 = @"
                    SELECT d.DepartmentName, e.FirstName, e.LastName, e.Salary
                    FROM Employees e
                    INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID
                    ORDER BY d.DepartmentName, e.Salary DESC;";
                DataTable dt4 = ExecuteQuery(connection, sql4);
                PrintDataTable(dt4, "4) Сотрудники с названиями отделов (INNER JOIN)");

                // 5. LEFT JOIN (глава 3)
                string sql5 = @"
                    SELECT e.FirstName, e.LastName, d.DepartmentName
                    FROM Employees e
                    LEFT JOIN Departments d ON e.DepartmentID = d.DepartmentID;";
                DataTable dt5 = ExecuteQuery(connection, sql5);
                PrintDataTable(dt5, "5) Все сотрудники с отделами (LEFT JOIN)");

                // 6. GROUP BY + COUNT (глава 4)
                string sql6 = @"
                    SELECT d.DepartmentName, COUNT(*) AS EmployeeCount
                    FROM Employees e
                    JOIN Departments d ON e.DepartmentID = d.DepartmentID
                    GROUP BY d.DepartmentName;";
                DataTable dt6 = ExecuteQuery(connection, sql6);
                PrintDataTable(dt6, "6) Количество сотрудников по отделам (GROUP BY)");

                // 7. GROUP BY + AVG + HAVING (глава 4)
                string sql7 = @"
                    SELECT d.DepartmentName, AVG(e.Salary) AS AvgSalary
                    FROM Employees e
                    JOIN Departments d ON e.DepartmentID = d.DepartmentID
                    GROUP BY d.DepartmentName
                    HAVING AVG(e.Salary) > 70000;";
                DataTable dt7 = ExecuteQuery(connection, sql7);
                PrintDataTable(dt7, "7) Отделы со средней зарплатой > 70000 (HAVING)");

                // 8. Подзапрос (глава 5)
                string sql8 = @"
                    SELECT FirstName, Salary
                    FROM Employees
                    WHERE Salary > (SELECT AVG(Salary) FROM Employees);";
                DataTable dt8 = ExecuteQuery(connection, sql8);
                PrintDataTable(dt8, "8) Сотрудники с зарплатой выше средней (подзапрос)");

                // 9. CTE (глава 5)
                string sql9 = @"
                    WITH DepartmentAverages AS (
                        SELECT DepartmentID, AVG(Salary) AS AvgSalary
                        FROM Employees
                        GROUP BY DepartmentID
                    )
                    SELECT e.FirstName, e.Salary, d.AvgSalary
                    FROM Employees e
                    JOIN DepartmentAverages d ON e.DepartmentID = d.DepartmentID
                    WHERE e.Salary > d.AvgSalary;";
                DataTable dt9 = ExecuteQuery(connection, sql9);
                PrintDataTable(dt9, "9) Сотрудники с зарплатой выше средней по отделу (CTE)");

                // 10. Оконная функция ROW_NUMBER() (глава 5)
                string sql10 = @"
                    SELECT FirstName, DepartmentID,
                        ROW_NUMBER() OVER (PARTITION BY DepartmentID ORDER BY Salary DESC) AS RankInDept
                    FROM Employees;";
                DataTable dt10 = ExecuteQuery(connection, sql10);
                PrintDataTable(dt10, "10) Ранжирование сотрудников по зарплате внутри отдела (ROW_NUMBER)");

                Console.WriteLine("Демонстрация завершена.");
            }
        }
    }
}