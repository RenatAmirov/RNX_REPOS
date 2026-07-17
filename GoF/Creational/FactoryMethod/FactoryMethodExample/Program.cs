using System;

namespace FactoryMethodExample
{
    // 1. Абстрактный продукт (интерфейс или абстрактный класс)
    // Определяет общий интерфейс для всех продуктов, создаваемых фабрикой.
    public interface IChart
    {
        void GenerateChart();
    }

    // 2. Конкретные продукты
    // Реализуют интерфейс продукта. 
    // Каждый продукт предоставляет свою реализацию метода GenerateChart().
    public class BarChart : IChart
    {
        public void GenerateChart()
        {
            Console.WriteLine("Генерация столбчатой диаграммы...");
        }
    }

    public class PieChart : IChart
    {
        public void GenerateChart()
        {
            Console.WriteLine("Генерация круговой диаграммы...");
        }
    }

    // 3. Абстрактный создатель (интерфейс или абстрактный класс)
    // Определяет фабричный метод, который возвращает продукт.
    // Подклассы будут переопределять этот метод для создания конкретных продуктов.
    public interface IChartProvider
    {
        IChart GetChart(); // Фабричный метод
    }

    // 4. Конкретные создатели
    // Реализуют фабричный метод, возвращая конкретный продукт.
    public class FreeChartProvider : IChartProvider
    {
        // Бесплатный провайдер возвращает столбчатую диаграмму
        public IChart GetChart()
        {
            return new BarChart();
        }
    }

    public class PaidChartProvider : IChartProvider
    {
        // Платный провайдер возвращает круговую диаграмму
        public IChart GetChart()
        {
            return new PieChart();
        }
    }

    // 5. Клиентский код
    // Использует абстрактный создатель и продукт.
    // Клиент не знает, какой конкретный продукт будет создан, 
    // это решается на этапе выбора провайдера.
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Демонстрация паттерна Фабричный метод ===\n");

            // Создаем фабрики (провайдеры)
            // В реальном приложении выбор фабрики может зависеть от конфигурации,
            // прав пользователя или других условий.
            IChartProvider freeProvider = new FreeChartProvider();
            IChartProvider paidProvider = new PaidChartProvider();

            // Получаем продукты через фабричный метод
            IChart chart1 = freeProvider.GetChart();
            IChart chart2 = paidProvider.GetChart();

            // Работаем с продуктами через общий интерфейс
            Console.WriteLine("Бесплатная версия:");
            chart1.GenerateChart(); // Выведет: Генерация столбчатой диаграммы...

            Console.WriteLine("\nПлатная версия:");
            chart2.GenerateChart(); // Выведет: Генерация круговой диаграммы...

            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}