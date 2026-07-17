// Подключаем пространство имён System, которое содержит базовые типы (например, Console, Decimal).
using System;

// Объявляем пространство имён для нашего проекта, чтобы логически сгруппировать классы.
namespace OpenClosedPrincipleDemo
{
    // Класс Program – точка входа в консольное приложение.
    class Program
    {
        // Метод Main – точка входа, с которой начинается выполнение программы.
        static void Main(string[] args)
        {
            // Выводим заголовок, поясняющий, что демонстрируется принцип OCP.
            Console.WriteLine("=== Демонстрация принципа открытости/закрытости (OCP) ===\n");

            // Вызываем метод, демонстрирующий проблемный код (без соблюдения OCP).
            DemonstrateWithoutOCP();

            // Разделитель для наглядности вывода.
            Console.WriteLine("\n---\n");

            // Вызываем метод, демонстрирующий правильное решение (с соблюдением OCP).
            DemonstrateWithOCP();

            // Ожидаем нажатия клавиши, чтобы окно консоли не закрылось сразу.
            Console.ReadKey();
        }

        // Метод, показывающий код, нарушающий OCP.
        static void DemonstrateWithoutOCP()
        {
            Console.WriteLine("1. НАРУШЕНИЕ OCP (ПЛОХОЙ ПРИМЕР)");
            Console.WriteLine("--------------------------------");

            // Создаём объект плохого калькулятора налогов, который содержит switch по странам.
            BadTaxCalculator badCalculator = new BadTaxCalculator();

            // Переменная, хранящая доход для расчёта.
            decimal income = 1000m;

            // Вычисляем налог для США, передавая строку "US".
            decimal usTax = badCalculator.Calculate(income, "US");
            // Выводим результат на консоль.
            Console.WriteLine($"Налог для США (доход {income}): {usTax}");

            // Вычисляем налог для Великобритании, передавая строку "UK".
            decimal ukTax = badCalculator.Calculate(income, "UK");
            // Выводим результат.
            Console.WriteLine($"Налог для UK (доход {income}): {ukTax}");

            // Пытаемся вычислить налог для Германии (строки "DE").
            // Этот код пока работает, потому что мы вручную добавили обработку "DE" в switch,
            // но если понадобится новая страна – придётся снова модифицировать класс BadTaxCalculator,
            // что нарушает OCP (класс не закрыт для модификации).
            decimal deTax = badCalculator.Calculate(income, "DE");
            Console.WriteLine($"Налог для DE (доход {income}): {deTax}");
        }

        // Метод, показывающий правильное решение с полиморфизмом и интерфейсами.
        static void DemonstrateWithOCP()
        {
            Console.WriteLine("2. СОБЛЮДЕНИЕ OCP (ХОРОШИЙ ПРИМЕР)");
            Console.WriteLine("-----------------------------------");

            // Доход для расчёта.
            decimal income = 1000m;

            // Создаём объект калькулятора для США (реализует интерфейс ICountryTaxCalculator).
            ICountryTaxCalculator usCalculator = new TaxCalculatorForUS();
            // Вызываем статический метод CalculateTax, передавая интерфейсный объект и доход.
            decimal usTax = TaxCalculator.CalculateTax(usCalculator, income);
            // Выводим результат.
            Console.WriteLine($"Налог для США (доход {income}): {usTax}");

            // Создаём объект калькулятора для Великобритании.
            ICountryTaxCalculator ukCalculator = new TaxCalculatorForUK();
            // Вычисляем налог через тот же метод, передавая уже другую реализацию интерфейса.
            decimal ukTax = TaxCalculator.CalculateTax(ukCalculator, income);
            Console.WriteLine($"Налог для UK (доход {income}): {ukTax}");

            // Создаём объект калькулятора для Германии (новая страна!).
            // Класс TaxCalculatorForGermany мы добавили позже, но при этом не изменили
            // ни строчки в классе TaxCalculator – он остался закрытым для модификации,
            // но открытым для расширения (мы просто добавили новый класс).
            ICountryTaxCalculator deCalculator = new TaxCalculatorForGermany();
            decimal deTax = TaxCalculator.CalculateTax(deCalculator, income);
            Console.WriteLine($"Налог для DE (доход {income}): {deTax}");
        }
    }

    // ПЛОХОЙ ПРИМЕР: класс нарушает OCP, потому что при добавлении новой страны
    // приходится изменять метод Calculate (добавлять новый case в switch).
    public class BadTaxCalculator
    {
        // Метод рассчитывает налог на основе страны, переданной строкой.
        // income – доход, country – строковый код страны.
        public decimal Calculate(decimal income, string country)
        {
            // Конструкция switch проверяет значение строки country.
            switch (country)
            {
                // Если страна "US" – применяем налоговую ставку США (30%).
                case "US":
                    // Возвращаем 30% от дохода.
                    return income * 0.3m;
                // Если страна "UK" – ставка 20%.
                case "UK":
                    return income * 0.2m;
                // Если страна "DE" – ставка 25% (добавлено позже – пример модификации).
                case "DE":
                    return income * 0.25m;
                // Для всех остальных стран – заглушка.
                default:
                    // Возвращаем 0, если страна не поддерживается.
                    return 0;
            }
        }
    }

    // ХОРОШИЙ ПРИМЕР: интерфейс, описывающий контракт для калькулятора налога страны.
    // Каждый новый калькулятор будет реализовывать этот интерфейс, не затрагивая существующий код.
    public interface ICountryTaxCalculator
    {
        // Метод, который должен вернуть сумму налога для заданного дохода.
        // income – доход, для которого считается налог.
        decimal CalculateTax(decimal income);
    }

    // Реализация интерфейса для США.
    public class TaxCalculatorForUS : ICountryTaxCalculator
    {
        // Конкретная реализация метода CalculateTax для налоговой системы США.
        // income – доход.
        public decimal CalculateTax(decimal income)
        {
            // Налоговая ставка США: 30%.
            return income * 0.3m;
        }
    }

    // Реализация интерфейса для Великобритании.
    public class TaxCalculatorForUK : ICountryTaxCalculator
    {
        // Реализация для UK.
        public decimal CalculateTax(decimal income)
        {
            // Налоговая ставка UK: 20%.
            return income * 0.2m;
        }
    }

    // НОВАЯ РЕАЛИЗАЦИЯ ДЛЯ ГЕРМАНИИ – добавляется БЕЗ изменения существующих классов.
    // Мы просто создаём новый класс, реализующий ICountryTaxCalculator.
    // Класс TaxCalculator (ниже) остаётся нетронутым – он закрыт для модификации,
    // но открыт для расширения через этот новый класс.
    public class TaxCalculatorForGermany : ICountryTaxCalculator
    {
        // Реализация для Германии.
        public decimal CalculateTax(decimal income)
        {
            // Налоговая ставка Германии: 25%.
            return income * 0.25m;
        }
    }

    // Статический класс, который использует полиморфизм для расчёта налога.
    // Он принимает интерфейс ICountryTaxCalculator вместо конкретной страны,
    // что позволяет добавлять новые страны без изменения этого класса.
    public static class TaxCalculator
    {
        // Метод CalculateTax принимает:
        // calculator – объект, реализующий ICountryTaxCalculator (стратегия расчёта),
        // income – облагаемый доход.
        // Возвращает сумму налога.
        public static decimal CalculateTax(ICountryTaxCalculator calculator, decimal income)
        {
            // Вызываем у переданного объекта метод CalculateTax – полиморфный вызов.
            // Какой именно метод вызовется, зависит от конкретной реализации интерфейса,
            // переданной в параметре calculator.
            return calculator.CalculateTax(income);
        }
    }
}