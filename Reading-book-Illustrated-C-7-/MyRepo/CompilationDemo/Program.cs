using System;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

namespace CompilationDemo
{
    class Program
    {
        // Точка входа — управляемый метод, который будет скомпилирован JIT при запуске.
        static void Main(string[] args)
        {
            // ================================================================
            // 1. Assembly — сборка, полученная после компиляции исходного кода.
            //    Сборка содержит CIL-инструкции и метаданные (типы, методы, строки).
            //    Здесь мы получаем объект Assembly текущего исполняемого файла.
            // ================================================================
            Assembly currentAssembly = Assembly.GetExecutingAssembly();
            Console.WriteLine($"Сборка: {currentAssembly.GetName().Name}");
            Console.WriteLine($"Расположение: {currentAssembly.Location}\n");

            // ================================================================
            // 2. Common Intermediate Language (CIL)
            //    Исходный C# был скомпилирован в CIL компилятором Roslyn.
            //    CIL хранится внутри сборки. Мы не можем увидеть его напрямую,
            //    но можем продемонстрировать метаданные, которые тоже там лежат.
            // ================================================================
            Type programType = typeof(Program);
            Console.WriteLine("Метаданные типа Program из CIL-сборки:");
            foreach (var method in programType.GetMethods(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static | BindingFlags.Instance))
            {
                Console.WriteLine($"  Метод: {method.Name}, атрибуты: {method.Attributes}");
            }
            Console.WriteLine();

            // ================================================================
            // 3. Just-In-Time (JIT) компиляция
            //    Прямо сейчас CLR еще не скомпилировала метод JitExample в машинный код.
            //    JIT-компилятор сделает это при первом вызове метода.
            //    Атрибут [MethodImpl(MethodImplOptions.NoInlining)] запрещает подстановку
            //    тела метода в точку вызова, гарантируя отдельную JIT-компиляцию.
            // ================================================================
            Console.WriteLine("Вызов метода, который будет скомпилирован JIT...");
            JitExample(); // Здесь происходит JIT-компиляция метода в машинный код
            Console.WriteLine("Метод выполнен (после JIT-компиляции).\n");

            // ================================================================
            // 4. Управляемый код (Managed Code)
            //    Весь код на C#, который мы пишем, выполняется под управлением CLR.
            //    CLR предоставляет сборку мусора, безопасность типов, обработку исключений.
            //    Следующий метод полностью управляемый.
            // ================================================================
            ManagedCodeExample();

            // ================================================================
            // 5. Неуправляемый код (Unmanaged Code)
            //    Код, выполняющийся вне CLR, например функции Win32 API.
            //    Вызов происходит через механизм P/Invoke.
            //    Требуется атрибут DllImport.
            // ================================================================
            Console.WriteLine("Вызов неуправляемого кода (MessageBox из user32.dll)...");
            UnmanagedCodeExample();
            Console.WriteLine("Неуправляемый код отработал.");
        }

        // Метод, который будет скомпилирован JIT при первом вызове.
        // NoInlining гарантирует, что JIT-компиляция не будет пропущена из-за инлайнинга.
        [MethodImpl(MethodImplOptions.NoInlining)]
        static void JitExample()
        {
            Console.WriteLine("  [JIT Example] Этот текст выводится уже скомпилированным машинным кодом.");
        }

        // Управляемый метод: выполняется полностью под контролем CLR.
        static void ManagedCodeExample()
        {
            Console.WriteLine("Управляемый код:");
            // CLR управляет памятью: выделяет и освобождает её.
            string message = "Привет из управляемого мира!";
            // Сборщик мусора автоматически удалит неиспользуемые объекты.
            Console.WriteLine($"  {message} (GC позаботится о строке)\n");
        }

        // Объявление неуправляемой функции из Win32 DLL.
        // DllImport указывает CLR загрузить user32.dll и найти функцию MessageBox.
        [DllImport("user32.dll", CharSet = CharSet.Unicode)]
        static extern int MessageBox(IntPtr hWnd, string text, string caption, uint type);

        // Метод, вызывающий неуправляемый код.
        static void UnmanagedCodeExample()
        {
            // Здесь происходит переход из управляемой среды в неуправляемую.
            // CLR маршалирует параметры (строки в нужный формат) и вызывает Win32 функцию.
            MessageBox(IntPtr.Zero, "Это сообщение от неуправляемого кода (Win32 API)", "Демонстрация", 0);
        }
    }
}