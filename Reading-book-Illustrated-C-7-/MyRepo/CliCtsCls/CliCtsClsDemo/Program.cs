// ================================================================
// ПРОЕКТ: CliCtsClsDemo
// НАЗНАЧЕНИЕ: Демонстрация CLI, CTS и CLS в .NET на примере C#.
// ================================================================
// Подключаем пространство имён System, где определены базовые типы CTS.
using System;


// Указываем, что вся сборка должна быть совместима с CLS.
// CLS (Common Language Specification) — набор правил, гарантирующих,
// что код можно использовать из любого .NET-языка.
// Если в публичном API встретится не-CLS-тип (например, uint),
// компилятор выдаст предупреждение (warning).
[assembly: CLSCompliant(true)]

// Объявляем пространство имён для нашего приложения.
namespace CliCtsClsDemo
{
    /// <summary>
    /// Пример класса, демонстрирующего CLS-совместимость.
    /// Все публичные члены используют типы, входящие в CLS (подмножество CTS).
    /// </summary>
    public class Car
    {
        // Поле: Brand — CLS-совместимый тип string (System.String).
        // String — ссылочный тип, определён в CTS и включён в CLS.
        public string Brand;

        // Поле: Year — CLS-совместимый тип int (System.Int32).
        // Int32 — 32-битное знаковое целое, входит и в CTS, и в CLS.
        public int Year;

        // Конструктор класса. Параметры также CLS-совместимы.
        public Car(string brand, int year)
        {
            // Присваиваем полям значения, переданные при создании объекта.
            Brand = brand;
            Year = year;
        }

        // Публичный метод, возвращающий void (System.Void в CTS) — это допустимо.
        public void Honk()
        {
            // Вывод строки в консоль. string — CLS-тип.
            Console.WriteLine($"{Brand} сигналит: Бип-бип!");
        }
    }

    /// <summary>
    /// Главный класс программы. Точка входа.
    /// </summary>
    class Program
    {
        /// <summary>
        /// Метод Main — точка входа, с которой начинается выполнение.
        /// CLI (Common Language Infrastructure) определяет, что исполнение
        /// стартует с метода Main (или аналога в других языках).
        /// </summary>
        /// <param name="args">Аргументы командной строки (string[] — CLS-тип).</param>
        static void Main(string[] args)
        {
            // ============================================================
            // 1. Common Language Infrastructure (CLI)
            //    CLI — это стандарт архитектуры .NET, описывающий среду исполнения.
            //    Наша программа после компиляции превратится в CIL-код (Common Intermediate Language),
            //    который будет выполнен CLR (Common Language Runtime) — реализацией CLI.
            // ============================================================
            Console.WriteLine("Демонстрация CLI, CTS и CLS в C#");
            Console.WriteLine("====================================");

            // CTS (Common Type System) — система типов, общая для всех языков .NET.
            // Все типы, используемые ниже, описаны в CTS.
            // В CTS входят и value-типы (int, double, bool), и reference-типы (string, object, классы).

            // Создаём экземпляр класса Car, который определён выше.
            // Car — это reference type (класс). Переменная myCar хранит ссылку на объект в куче.
            Car myCar = new Car("Toyota", 2024);

            // Доступ к полям объекта. Поля Brand (string) и Year (int) — CTS-типы.
            // string — псевдоним C# для System.String; int — для System.Int32.
            Console.WriteLine($"Марка: {myCar.Brand}, Год выпуска: {myCar.Year}");

            // Вызов метода Honk(), возвращающего void (System.Void).
            myCar.Honk();

            // Работа с типами значений CTS.
            // double (System.Double) — 64-битное число с плавающей точкой.
            double price = 25000.50;

            // bool (System.Boolean) — логический тип.
            bool isElectric = false;

            // DateTime — структура из CTS, не является примитивом C#, но входит в CTS.
            DateTime productionDate = new DateTime(2024, 5, 20);

            // Вывод информации с использованием CTS-типов.
            Console.WriteLine($"Цена: {price} USD, Электро: {isElectric}, Дата производства: {productionDate.ToShortDateString()}");

            // ============================================================
            // 2. Common Type System (CTS)
            //    Все типы, использованные выше (int, string, bool, double, DateTime, void, класс Car),
            //    являются частью CTS. Благодаря этому любой .NET-язык (F#, VB.NET) может
            //    оперировать теми же типами, хотя синтаксис разный.
            // ============================================================
            Console.WriteLine("\n--- Пример CTS: типы едины для всех языков .NET ---");
            // int в C# — это System.Int32, в VB.NET — Integer, в F# — int.
            // Однако в скомпилированном CIL-коде это один и тот же тип.
            int ctsInt = 42;            // System.Int32
            string ctsString = "Hello"; // System.String
            bool ctsBool = true;        // System.Boolean
            Console.WriteLine($"int = {ctsInt}, string = {ctsString}, bool = {ctsBool}");

            // ============================================================
            // 3. Common Language Specification (CLS)
            //    CLS — подмножество CTS, которое должно поддерживаться всеми языками.
            //    Атрибут [assembly: CLSCompliant(true)] требует, чтобы публичные
            //    члены (классы, методы, поля) использовали только CLS-типы.
            // ============================================================
            Console.WriteLine("\n--- Пример CLS-совместимости ---");
            // Класс Car полностью CLS-совместим:
            //  - публичные поля Brand (string) и Year (int) — CLS-типы.
            //  - метод Honk() возвращает void — CLS-тип.
            //  - конструктор принимает string и int.
            Console.WriteLine("Класс Car является CLS-совместимым.");

            // Попытка добавить публичное поле с не-CLS-типом (например, uint)
            // при включённом атрибуте [assembly: CLSCompliant(true)] вызвала бы
            // предупреждение компилятора:
            //   warning CS3001: Argument type 'uint' is not CLS-compliant
            //   warning CS3003: Type of 'Car.Mileage' is not CLS-compliant
            //
            // В коде это закомментировано, чтобы проект собирался без предупреждений:
            // public uint Mileage;   // uint не входит в CLS, только в CTS

            // Таким образом, CLS гарантирует, что сборку можно использовать из любого
            // языка .NET, избегая типов, специфичных для одного языка (например, uint в C#).

            // ============================================================
            // ИТОГ:
            // CLI — стандарт среды (CIL + метаданные + исполнение).
            // CTS — общая система типов.
            // CLS — правила совместимости языков (подмножество CTS).
            // ============================================================
            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}