using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace BridgePatternDemo
{
    // =====================================================================
    // 1. Модель данных (Customer) – упрощённая версия для демонстрации
    // =====================================================================
    public class Customer
    {
        public string CustomerID { get; set; }
        public string CompanyName { get; set; }
        public string ContactName { get; set; } 
        public string Country { get; set; }
    }

    // =====================================================================
    // 2. Абстракция «логгер ошибок» (интерфейс) – одна из двух сторон моста
    // =====================================================================
    public interface IErrorLogger
    {
        /// <summary>
        /// Логирует сообщение об ошибке.
        /// </summary>
        /// <param name="message">Текст ошибки</param>
        void Log(string message);
    }

    // =====================================================================
    // 3. Конкретные реализации логгеров – первая ветвь моста
    // =====================================================================

    /// <summary>
    /// Логирование в текстовый файл.
    /// </summary>
    public class TextFileErrorLogger : IErrorLogger
    {
        private readonly string _filePath;

        public TextFileErrorLogger(string filePath = "errorlog.txt")
        {
            _filePath = filePath;
        }

        public void Log(string message)
        {
            // Добавляем временную метку и переводим строку
            string logEntry = $"[{DateTime.Now:yyyy-MM-dd HH:mm:ss}] {message}\n";
            // Дописываем в конец файла (если файла нет – он создаётся)
            File.AppendAllText(_filePath, logEntry);
            // Для наглядности дублируем в консоль
            Console.WriteLine($"Лог (текст): {logEntry.Trim()}");
        }
    }

    /// <summary>
    /// Логирование в XML-файл.
    /// </summary>
    public class XmlErrorLogger : IErrorLogger
    {
        private readonly string _filePath;

        public XmlErrorLogger(string filePath = "errorlog.xml")
        {
            _filePath = filePath;
        }

        public void Log(string message)
        {
            // Формируем XML-элемент
            string logEntry = $"<error><message>{message}</message><timestamp>{DateTime.Now:yyyy-MM-dd HH:mm:ss}</timestamp></error>\n";
            File.AppendAllText(_filePath, logEntry);
            Console.WriteLine($"Лог (XML): {logEntry.Trim()}");
        }
    }

    // =====================================================================
    // 4. Абстракция «импортёр данных» (интерфейс) – вторая сторона моста
    // =====================================================================
    public interface IDataImporter
    {
        /// <summary>
        /// Логгер, который будет использоваться для записи ошибок.
        /// </summary>
        IErrorLogger ErrorLogger { get; set; }

        /// <summary>
        /// Импортирует список клиентов (имитация).
        /// </summary>
        void Import(List<Customer> customers);
    }

    // =====================================================================
    // 5. Конкретные реализации импортёров – вторая ветвь моста
    // =====================================================================

    /// <summary>
    /// Базовая версия импортёра – имитирует простой импорт.
    /// </summary>
    public class DataImporterBasic : IDataImporter
    {
        public IErrorLogger ErrorLogger { get; set; }

        public void Import(List<Customer> customers)
        {
            try
            {
                Console.WriteLine("Начинается базовый импорт...");
                foreach (var customer in customers)
                {
                    // Имитация обработки (например, проверка или вставка в БД)
                    Console.WriteLine($"  Обработка: {customer.CustomerID} - {customer.CompanyName}");
                    // Здесь может возникнуть ошибка, например, при пустом CustomerID
                    if (string.IsNullOrEmpty(customer.CustomerID))
                        throw new Exception("CustomerID не может быть пустым!");
                }
                Console.WriteLine("Базовый импорт завершён успешно.");
            }
            catch (Exception ex)
            {
                // Если произошла ошибка – логируем через присвоенный логгер
                ErrorLogger?.Log($"Ошибка при базовом импорте: {ex.Message}");
                throw; // пробрасываем дальше, чтобы вызывающий код знал о проблеме
            }
        }
    }

    /// <summary>
    /// Расширенная версия импортёра – добавляет дополнительную логику (например, валидацию).
    /// </summary>
    public class DataImporterAdvanced : IDataImporter
    {
        public IErrorLogger ErrorLogger { get; set; }

        public void Import(List<Customer> customers)
        {
            try
            {
                Console.WriteLine("Начинается расширенный импорт...");
                foreach (var customer in customers)
                {
                    // Дополнительные проверки, характерные для «продвинутой» версии
                    Console.WriteLine($"  Расширенная обработка: {customer.CustomerID} - {customer.CompanyName} - {customer.Country}");
                    if (customer.Country?.Length > 20)
                        throw new Exception("Название страны слишком длинное!");
                }
                Console.WriteLine("Расширенный импорт завершён успешно.");
            }
            catch (Exception ex)
            {
                ErrorLogger?.Log($"Ошибка при расширенном импорте: {ex.Message}");
                throw;
            }
        }
    }

    // =====================================================================
    // 6. Точка входа – демонстрация работы паттерна Мост
    // =====================================================================
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Демонстрация паттерна Мост (Bridge) ===\n");

            // Подготавливаем тестовые данные (список клиентов)
            var customers = new List<Customer>
            {
                new Customer { CustomerID = "ALFKI", CompanyName = "Alfreds Futterkiste", ContactName = "Maria Anders", Country = "Germany" },
                new Customer { CustomerID = "", CompanyName = "Empty ID", ContactName = "Test", Country = "USA" }, // этот вызовет ошибку
                new Customer { CustomerID = "ANATR", CompanyName = "Ana Trujillo", ContactName = "Ana Trujillo", Country = "Mexico" }
            };

            // =============================================================
            // Вариант 1: Базовый импортёр + текстовый логгер
            // =============================================================
            Console.WriteLine("--- Вариант 1: BasicImporter + TextLogger ---");
            IDataImporter importer1 = new DataImporterBasic();
            importer1.ErrorLogger = new TextFileErrorLogger("log_basic_text.txt");
            try
            {
                importer1.Import(customers);
            }
            catch
            {
                // Игнорируем, чтобы продолжить демонстрацию
            }

            Console.WriteLine("\n--- Вариант 2: BasicImporter + XmlLogger ---");
            // =============================================================
            // Вариант 2: Базовый импортёр + XML-логгер (меняем реализацию логгера)
            // =============================================================
            IDataImporter importer2 = new DataImporterBasic();
            importer2.ErrorLogger = new XmlErrorLogger("log_basic_xml.xml");
            try
            {
                importer2.Import(customers);
            }
            catch { }

            Console.WriteLine("\n--- Вариант 3: AdvancedImporter + TextLogger ---");
            // =============================================================
            // Вариант 3: Расширенный импортёр + текстовый логгер (меняем импортёр)
            // =============================================================
            IDataImporter importer3 = new DataImporterAdvanced();
            importer3.ErrorLogger = new TextFileErrorLogger("log_advanced_text.txt");
            try
            {
                importer3.Import(customers);
            }
            catch { }

            Console.WriteLine("\n--- Вариант 4: AdvancedImporter + XmlLogger ---");
            // =============================================================
            // Вариант 4: Расширенный импортёр + XML-логгер (полная смена обеих ветвей)
            // =============================================================
            IDataImporter importer4 = new DataImporterAdvanced();
            importer4.ErrorLogger = new XmlErrorLogger("log_advanced_xml.xml");
            try
            {
                importer4.Import(customers);
            }
            catch { }

            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}