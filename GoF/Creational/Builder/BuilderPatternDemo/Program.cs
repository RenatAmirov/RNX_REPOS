namespace BuilderPatternDemo
{
    // ============================================================
    // Проект: BuilderPatternDemo
    // Описание: Демонстрация паттерна "Строитель" (Builder) на C#
    // На основе примера из книги "Beginning SOLID Principles and 
    // Design Patterns for ASP.NET Developers" (Глава 4)
    // ============================================================

    using System;
    using System.Collections.Generic;

    // -------------------- Модели данных --------------------

    /// <summary>
    /// Класс, представляющий одну деталь компьютера.
    /// В оригинальном примере использовалась база данных,
    /// здесь мы храним данные прямо в объекте.
    /// </summary>
    public class ComputerPart
    {
        /// <summary>
        /// Название детали (например, "CPU", "Cabinet").
        /// </summary>
        public string PartName { get; set; }

        /// <summary>
        /// Код детали (артикул или описание).
        /// </summary>
        public string PartCode { get; set; }

        /// <summary>
        /// Вывод информации о детали в удобочитаемом виде.
        /// </summary>
        public override string ToString()
        {
            return $"{PartName}: {PartCode}";
        }
    }

    /// <summary>
    /// Класс, представляющий готовый компьютер.
    /// Содержит список собранных деталей.
    /// </summary>
    public class Computer
    {
        /// <summary>
        /// Список деталей, из которых состоит компьютер.
        /// </summary>
        public List<ComputerPart> Parts { get; set; }

        /// <summary>
        /// Конструктор инициализирует пустой список.
        /// </summary>
        public Computer()
        {
            Parts = new List<ComputerPart>();
        }

        /// <summary>
        /// Вывод конфигурации компьютера в консоль.
        /// </summary>
        public void ShowConfiguration()
        {
            Console.WriteLine("Конфигурация компьютера:");
            foreach (var part in Parts)
            {
                Console.WriteLine($"  {part}");
            }
            Console.WriteLine();
        }
    }

    // -------------------- Интерфейс строителя --------------------

    /// <summary>
    /// Интерфейс строителя, определяющий шаги сборки компьютера.
    /// Каждый метод добавляет определённую деталь.
    /// </summary>
    public interface IComputerBuilder
    {
        /// <summary>Добавить процессор.</summary>
        void AddCPU();

        /// <summary>Добавить корпус.</summary>
        void AddCabinet();

        /// <summary>Добавить мышь.</summary>
        void AddMouse();

        /// <summary>Добавить клавиатуру.</summary>
        void AddKeyboard();

        /// <summary>Добавить монитор.</summary>
        void AddMonitor();

        /// <summary>Вернуть готовый компьютер после сборки.</summary>
        Computer GetComputer();
    }

    // -------------------- Конкретные строители --------------------

    /// <summary>
    /// Строитель для домашнего компьютера.
    /// Добавляет бюджетные детали.
    /// </summary>
    public class HomeComputerBuilder : IComputerBuilder
    {
        /// <summary>
        /// Ссылка на собираемый компьютер.
        /// </summary>
        private Computer _computer;

        /// <summary>
        /// Конструктор инициализирует новый компьютер.
        /// </summary>
        public HomeComputerBuilder()
        {
            _computer = new Computer();
        }

        public void AddCPU()
        {
            // Добавляем процессор с кодом "CPU-HOME"
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "CPU",
                PartCode = "Intel Celeron G5900 (Home)"
            });
        }

        public void AddCabinet()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "Cabinet",
                PartCode = "ATX Mini Tower (Home)"
            });
        }

        public void AddMouse()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "Mouse",
                PartCode = "Optical USB (Home)"
            });
        }

        public void AddKeyboard()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "Keyboard",
                PartCode = "Standard USB (Home)"
            });
        }

        public void AddMonitor()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "Monitor",
                PartCode = "19 inch LED (Home)"
            });
        }

        public Computer GetComputer()
        {
            // Возвращаем собранный компьютер
            return _computer;
        }
    }

    /// <summary>
    /// Строитель для офисного компьютера.
    /// Детали среднего уровня.
    /// </summary>
    public class OfficeComputerBuilder : IComputerBuilder
    {
        private Computer _computer;

        public OfficeComputerBuilder()
        {
            _computer = new Computer();
        }

        public void AddCPU()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "CPU",
                PartCode = "Intel Core i5-10400 (Office)"
            });
        }

        public void AddCabinet()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "Cabinet",
                PartCode = "Mid Tower ATX (Office)"
            });
        }

        public void AddMouse()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "Mouse",
                PartCode = "Wireless Optical (Office)"
            });
        }

        public void AddKeyboard()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "Keyboard",
                PartCode = "Wireless Keyboard (Office)"
            });
        }

        public void AddMonitor()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "Monitor",
                PartCode = "24 inch IPS (Office)"
            });
        }

        public Computer GetComputer()
        {
            return _computer;
        }
    }

    /// <summary>
    /// Строитель для компьютера разработчика.
    /// Детали высокой производительности.
    /// </summary>
    public class DevelopmentComputerBuilder : IComputerBuilder
    {
        private Computer _computer;

        public DevelopmentComputerBuilder()
        {
            _computer = new Computer();
        }

        public void AddCPU()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "CPU",
                PartCode = "Intel Core i9-11900K (Dev)"
            });
        }

        public void AddCabinet()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "Cabinet",
                PartCode = "Full Tower with RGB (Dev)"
            });
        }

        public void AddMouse()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "Mouse",
                PartCode = "Gaming Mouse (Dev)"
            });
        }

        public void AddKeyboard()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "Keyboard",
                PartCode = "Mechanical Keyboard (Dev)"
            });
        }

        public void AddMonitor()
        {
            _computer.Parts.Add(new ComputerPart
            {
                PartName = "Monitor",
                PartCode = "27 inch 4K (Dev)"
            });
        }

        public Computer GetComputer()
        {
            return _computer;
        }
    }

    // -------------------- Директор (Управляет процессом сборки) --------------------

    /// <summary>
    /// Класс-директор, который управляет процессом сборки.
    /// Он знает, в каком порядке вызывать методы строителя.
    /// </summary>
    public class ComputerAssembler
    {
        /// <summary>
        /// Ссылка на строителя, который будет использован для сборки.
        /// </summary>
        private IComputerBuilder _builder;

        /// <summary>
        /// Конструктор принимает конкретного строителя.
        /// </summary>
        /// <param name="builder">Экземпляр строителя (Home, Office, Dev).</param>
        public ComputerAssembler(IComputerBuilder builder)
        {
            _builder = builder;
        }

        /// <summary>
        /// Выполняет сборку компьютера, вызывая все шаги в правильном порядке.
        /// Возвращает готовый компьютер.
        /// </summary>
        public Computer AssembleComputer()
        {
            // Последовательность сборки фиксирована:
            // сначала процессор, затем корпус, монитор, клавиатура, мышь.
            _builder.AddCPU();
            _builder.AddCabinet();
            _builder.AddMonitor();
            _builder.AddKeyboard();
            _builder.AddMouse();

            // После добавления всех деталей возвращаем готовый продукт.
            return _builder.GetComputer();
        }
    }

    // -------------------- Клиентский код (Program) --------------------

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Демонстрация паттерна Строитель (Builder) ===\n");

            // 1. Создаём строителя для домашнего компьютера
            IComputerBuilder homeBuilder = new HomeComputerBuilder();
            // 2. Создаём директора и передаём ему строителя
            ComputerAssembler assembler = new ComputerAssembler(homeBuilder);
            // 3. Собираем компьютер
            Computer homeComputer = assembler.AssembleComputer();
            // 4. Выводим конфигурацию
            homeComputer.ShowConfiguration();

            // 5. То же самое для офисного компьютера
            IComputerBuilder officeBuilder = new OfficeComputerBuilder();
            assembler = new ComputerAssembler(officeBuilder);
            Computer officeComputer = assembler.AssembleComputer();
            officeComputer.ShowConfiguration();

            // 6. И для компьютера разработчика
            IComputerBuilder devBuilder = new DevelopmentComputerBuilder();
            assembler = new ComputerAssembler(devBuilder);
            Computer devComputer = assembler.AssembleComputer();
            devComputer.ShowConfiguration();

            Console.WriteLine("Нажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}
