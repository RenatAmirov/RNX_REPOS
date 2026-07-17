using System;

namespace AdapterPatternDemo
{
    // 1. Целевой интерфейс, с которым работает клиент
    //    Определяет метод, который ожидает клиент.
    public interface IChart
    {
        void Display();
    }

    // 2. Оригинальный класс (собственный компонент), 
    //    который уже реализует целевой интерфейс.
    public class MyChartGenerator : IChart
    {
        public void Display()
        {
            Console.WriteLine("Генерация диаграммы с помощью собственного компонента MyChartGenerator.");
        }
    }

    // 3. Сторонний класс с несовместимым интерфейсом.
    //    Клиент не может использовать его напрямую, т.к. ожидает IChart.
    public class ThirdPartyChartGenerator
    {
        // Метод стороннего компонента имеет другое имя и, возможно, другие параметры.
        public void DrawChart()
        {
            Console.WriteLine("Рисование диаграммы сторонним компонентом ThirdPartyChartGenerator.");
        }
    }

    // 4. Объектный адаптер (Object Adapter)
    //    Реализует целевой интерфейс, внутри содержит ссылку на адаптируемый объект.
    public class MyChartAdapter : IChart
    {
        private readonly ThirdPartyChartGenerator _adaptee;

        // В конструктор передаётся экземпляр адаптируемого класса.
        public MyChartAdapter(ThirdPartyChartGenerator adaptee)
        {
            _adaptee = adaptee;
        }

        // Реализация метода интерфейса IChart.
        // Делегирует вызов методу стороннего компонента.
        public void Display()
        {
            // Адаптер преобразует вызов Display() в вызов DrawChart().
            _adaptee.DrawChart();
        }
    }

    // 5. Классовый адаптер (Class Adapter)
    //    Наследует адаптируемый класс и реализует целевой интерфейс.
    //    В C# такое возможно, т.к. допускается наследование только одного класса.
    public class MyClassAdapter : ThirdPartyChartGenerator, IChart
    {
        // Реализуем метод интерфейса IChart.
        // Вызываем унаследованный метод DrawChart().
        public void Display()
        {
            // Так как мы унаследовали ThirdPartyChartGenerator,
            // мы можем напрямую вызывать его метод.
            DrawChart();
        }
    }

    // 6. Клиентский код (точка входа в приложение)
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Демонстрация паттерна Адаптер ===\n");

            // ---------- Использование собственного компонента ----------
            Console.WriteLine("1. Использование собственного компонента (без адаптера):");
            IChart ownComponent = new MyChartGenerator();
            ownComponent.Display();  // Вызов метода Display() напрямую

            Console.WriteLine();

            // ---------- Использование объектного адаптера ----------
            Console.WriteLine("2. Использование стороннего компонента через объектный адаптер:");
            // Создаём экземпляр стороннего компонента.
            ThirdPartyChartGenerator thirdParty = new ThirdPartyChartGenerator();
            // Создаём адаптер, передавая ему сторонний компонент.
            IChart adapterObject = new MyChartAdapter(thirdParty);
            // Клиент вызывает Display(), адаптер перенаправляет вызов на DrawChart().
            adapterObject.Display();

            Console.WriteLine();

            // ---------- Использование классового адаптера ----------
            Console.WriteLine("3. Использование стороннего компонента через классовый адаптер:");
            // Классовый адаптер сам является наследником ThirdPartyChartGenerator,
            // поэтому можно создать его напрямую.
            IChart adapterClass = new MyClassAdapter();
            // Клиент снова вызывает Display(), адаптер вызывает DrawChart().
            adapterClass.Display();

            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}