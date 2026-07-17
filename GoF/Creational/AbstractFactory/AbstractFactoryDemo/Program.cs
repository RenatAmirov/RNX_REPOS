using System;
using System.Collections.Generic;

namespace AbstractFactoryDemo
{
    // ==================== Абстрактные классы для семейства объектов ====================

    /// <summary>
    /// Абстрактный класс, представляющий соединение с базой данных.
    /// </summary>
    public abstract class DbConnection
    {
        public string ConnectionString { get; set; }
        public abstract void Open();
        public abstract void Close();
    }

    /// <summary>
    /// Абстрактный класс, представляющий команду к базе данных.
    /// </summary>
    public abstract class DbCommand
    {
        public string CommandText { get; set; }
        public DbConnection Connection { get; set; }
        public abstract void ExecuteNonQuery();        // для INSERT/UPDATE/DELETE
        public abstract void ExecuteReader();          // для SELECT (в нашем примере просто вывод)
    }

    /// <summary>
    /// Абстрактный класс, представляющий параметр команды.
    /// </summary>
    public abstract class DbParameter
    {
        public string ParameterName { get; set; }
        public object Value { get; set; }
    }

    // ==================== Интерфейс абстрактной фабрики ====================

    /// <summary>
    /// Интерфейс фабрики, создающей семейство связанных объектов:
    /// соединение, команду, параметр.
    /// </summary>
    public interface IDatabaseFactory
    {
        DbConnection CreateConnection();
        DbCommand CreateCommand();
        DbParameter CreateParameter();
    }

    // ==================== Реализация для SQL Server (SqlClient) ====================

    /// <summary>
    /// Конкретное соединение для SQL Server.
    /// </summary>
    public class SqlConnection : DbConnection
    {
        public override void Open()
        {
            Console.WriteLine($"SqlConnection открыто с строкой: {ConnectionString}");
        }

        public override void Close()
        {
            Console.WriteLine("SqlConnection закрыто.");
        }
    }

    /// <summary>
    /// Конкретная команда для SQL Server.
    /// </summary>
    public class SqlCommand : DbCommand
    {
        public override void ExecuteNonQuery()
        {
            Console.WriteLine($"SqlCommand выполняет не-запрос: {CommandText}");
        }

        public override void ExecuteReader()
        {
            Console.WriteLine($"SqlCommand выполняет чтение: {CommandText}");
        }
    }

    /// <summary>
    /// Конкретный параметр для SQL Server.
    /// </summary>
    public class SqlParameter : DbParameter
    {
        // Никакой дополнительной логики не требуется
    }

    /// <summary>
    /// Фабрика для SQL Server, реализующая интерфейс IDatabaseFactory.
    /// </summary>
    public class SqlClientFactory : IDatabaseFactory
    {
        public DbConnection CreateConnection()
        {
            return new SqlConnection();
        }

        public DbCommand CreateCommand()
        {
            return new SqlCommand();
        }

        public DbParameter CreateParameter()
        {
            return new SqlParameter();
        }
    }

    // ==================== Реализация для OLE DB (OleDb) ====================

    /// <summary>
    /// Конкретное соединение для OLE DB.
    /// </summary>
    public class OleDbConnection : DbConnection
    {
        public override void Open()
        {
            Console.WriteLine($"OleDbConnection открыто с строкой: {ConnectionString}");
        }

        public override void Close()
        {
            Console.WriteLine("OleDbConnection закрыто.");
        }
    }

    /// <summary>
    /// Конкретная команда для OLE DB.
    /// </summary>
    public class OleDbCommand : DbCommand
    {
        public override void ExecuteNonQuery()
        {
            Console.WriteLine($"OleDbCommand выполняет не-запрос: {CommandText}");
        }

        public override void ExecuteReader()
        {
            Console.WriteLine($"OleDbCommand выполняет чтение: {CommandText}");
        }
    }

    /// <summary>
    /// Конкретный параметр для OLE DB.
    /// </summary>
    public class OleDbParameter : DbParameter
    {
        // Никакой дополнительной логики не требуется
    }

    /// <summary>
    /// Фабрика для OLE DB, реализующая интерфейс IDatabaseFactory.
    /// </summary>
    public class OleDbFactory : IDatabaseFactory
    {
        public DbConnection CreateConnection()
        {
            return new OleDbConnection();
        }

        public DbCommand CreateCommand()
        {
            return new OleDbCommand();
        }

        public DbParameter CreateParameter()
        {
            return new OleDbParameter();
        }
    }

    // ==================== Клиентский код – DatabaseHelper ====================

    /// <summary>
    /// Класс-помощник для выполнения запросов к базе данных.
    /// Он получает фабрику (абстракцию) и использует её для создания объектов,
    /// не завися от конкретных реализаций.
    /// </summary>
    public class DatabaseHelper
    {
        private readonly IDatabaseFactory _factory;

        /// <summary>
        /// Конструктор принимает фабрику, которая будет использоваться для создания объектов.
        /// </summary>
        /// <param name="factory">Фабрика (SqlClient или OleDb).</param>
        public DatabaseHelper(IDatabaseFactory factory)
        {
            _factory = factory;
        }

        /// <summary>
        /// Выполняет запрос (SELECT) и выводит результаты (в нашем примере просто имитация).
        /// </summary>
        /// <param name="query">SQL-запрос.</param>
        public void ExecuteQuery(string query)
        {
            // 1. Создаём соединение с помощью фабрики
            DbConnection connection = _factory.CreateConnection();
            connection.ConnectionString = "Server=.;Database=Northwind;Integrated Security=true";
            connection.Open();

            // 2. Создаём команду с помощью фабрики
            DbCommand command = _factory.CreateCommand();
            command.Connection = connection;
            command.CommandText = query;

            // 3. Создаём параметры (демонстрация) – можно добавить параметры, если нужно
            // Например, создаём параметр для поиска по CustomerID
            DbParameter parameter = _factory.CreateParameter();
            parameter.ParameterName = "@CustomerID";
            parameter.Value = "ALFKI";
            // В реальном коде мы бы добавили параметр в коллекцию команды,
            // но для упрощения просто выведем информацию.

            // 4. Выполняем команду
            command.ExecuteReader();

            // 5. Закрываем соединение
            connection.Close();

            // Вывод информации о параметре (для демонстрации)
            Console.WriteLine($"Создан параметр: {parameter.ParameterName} = {parameter.Value}");
            Console.WriteLine();
        }

        /// <summary>
        /// Выполняет запрос, изменяющий данные (INSERT/UPDATE/DELETE).
        /// </summary>
        public void ExecuteNonQuery(string query)
        {
            DbConnection connection = _factory.CreateConnection();
            connection.ConnectionString = "Server=.;Database=Northwind;Integrated Security=true";
            connection.Open();

            DbCommand command = _factory.CreateCommand();
            command.Connection = connection;
            command.CommandText = query;

            command.ExecuteNonQuery();

            connection.Close();
            Console.WriteLine();
        }
    }

    // ==================== Точка входа в приложение ====================

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Демонстрация паттерна Абстрактная фабрика ===\n");

            // 1. Используем фабрику для SQL Server
            Console.WriteLine("--- Работа с SqlClient ---");
            IDatabaseFactory sqlFactory = new SqlClientFactory();
            DatabaseHelper sqlHelper = new DatabaseHelper(sqlFactory);
            sqlHelper.ExecuteQuery("SELECT * FROM Customers WHERE CustomerID = @CustomerID");

            // 2. Используем фабрику для OLE DB
            Console.WriteLine("--- Работа с OleDb ---");
            IDatabaseFactory oleFactory = new OleDbFactory();
            DatabaseHelper oleHelper = new DatabaseHelper(oleFactory);
            oleHelper.ExecuteQuery("SELECT * FROM Customers WHERE CustomerID = @CustomerID");

            // 3. Дополнительно: выполним запрос на изменение (для демонстрации)
            Console.WriteLine("--- Выполнение INSERT (SqlClient) ---");
            sqlHelper.ExecuteNonQuery("INSERT INTO Customers (CustomerID, CompanyName) VALUES ('NEW1', 'New Company')");

            Console.WriteLine("Нажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}