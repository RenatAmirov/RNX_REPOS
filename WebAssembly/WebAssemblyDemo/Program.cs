using System;
using Wasmtime; // Пространство имён библиотеки Wasmtime

namespace WebAssemblyDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Демонстрация основ WebAssembly (Wasm) на C# ===\n");

            // ---------- 1. Простой модуль сложения (WAT -> компиляция -> выполнение) ----------
            // Текст модуля на языке WAT (WebAssembly Text Format)
            string watAdd = @"
(module
  ;; Функция сложения двух i32 чисел, возвращает i32
  (func $add (param $lhs i32) (param $rhs i32) (result i32)
    local.get $lhs   ;; кладём на стек значение параметра $lhs
    local.get $rhs   ;; кладём на стек значение параметра $rhs
    i32.add          ;; инструкция складывает два верхних значения стека и кладёт результат
  )
  (export ""add"" (func $add))  ;; экспорт функции под именем 'add'
)";

            // Создаём движок Wasmtime — основной контекст выполнения
            using var engine = new Engine();

            // Компилируем WAT-текст в исполняемый модуль
            using var moduleAdd = Module.FromText(engine, "add_module", watAdd);

            // Создаём хранилище (Store) для состояния экземпляра модуля
            using var storeAdd = new Store(engine);

            // Инстанцируем модуль — связываем скомпилированный код с состоянием
            var instanceAdd = new Instance(storeAdd, moduleAdd);

            // Получаем ссылку на экспортированную функцию "add"
            var addFunc = instanceAdd.GetFunction<int, int, int>("add");

            // Вызываем функцию из C#: 5 + 7 = 12
            int resultAdd = addFunc(5, 7);
            Console.WriteLine($"Сложение: 5 + 7 = {resultAdd}");

            // ---------- 2. Локальные переменные, глобальные переменные, условная логика, циклы ----------
            // Создаём более сложный модуль
            string watAdvanced = @"
(module
  ;; --- Глобальная изменяемая переменная (mut i32) ---
  (global $counter (mut i32) (i32.const 0))

  ;; Функция, увеличивающая глобальный счётчик на 1 и возвращающая новое значение
  (func $incCounter (result i32)
    global.get $counter   ;; текущее значение счётчика
    i32.const 1
    i32.add
    global.set $counter   ;; сохраняем обратно
    global.get $counter   ;; возвращаем новое значение
  )

  ;; Функция демонстрации локальной переменной и условного оператора if/else
  (func $isPositive (param $x i32) (result i32)
    (local $temp i32)          ;; локальная переменная
    local.get $x
    local.set $temp            ;; temp = x
    ;; if (temp > 0) return 1 else return 0
    local.get $temp
    i32.const 0
    i32.gt_s                  ;; знаковое сравнение: temp > 0 ?
    (if (result i32)          ;; блок if с результатом i32
      (then i32.const 1)
      (else i32.const 0)
    )
  )

  ;; Функция с циклом: вычисляет сумму чисел от 1 до n (n >= 0)
  (func $sumToN (param $n i32) (result i32)
    (local $acc i32)          ;; аккумулятор
    (local $i i32)            ;; счётчик цикла
    i32.const 0
    local.set $acc            ;; acc = 0
    i32.const 1
    local.set $i              ;; i = 1
    (loop $continue           ;; метка $continue для начала цикла
      ;; условие выхода: если i > n, перейти к блоку $done
      local.get $i
      local.get $n
      i32.gt_s
      (br_if $done)           ;; переход по метке $done, если условие истинно
      ;; тело цикла: acc = acc + i; i = i + 1
      local.get $acc
      local.get $i
      i32.add
      local.set $acc
      local.get $i
      i32.const 1
      i32.add
      local.set $i
      br $continue            ;; безусловный переход в начало цикла
    )
    local.get $acc             ;; возвращаем накопленную сумму
  )

  ;; --- Работа с линейной памятью ---
  (memory (export ""mem"") 1)   ;; 1 страница = 64 КБ, экспортируем память

  ;; Функция записи значения i32 по адресу (смещение 0)
  (func $store (param $val i32)
    i32.const 0               ;; адрес 0 (байты 0-3)
    local.get $val
    i32.store                 ;; сохраняем 4 байта
  )

  ;; Функция чтения значения i32 по адресу 0
  (func $load (result i32)
    i32.const 0
    i32.load                  ;; загружаем 4 байта
  )

  ;; Импорт функции из окружения (хоста) для логирования числа
  (import ""env"" ""log"" (func $log (param i32)))

  ;; Функция, которая читает число из памяти и вызывает импортированную функцию log
  (func $readAndLog
    i32.const 0
    i32.load                  ;; загружаем число из памяти
    call $log                 ;; вызываем внешнюю функцию логирования
  )

  ;; Экспортируем все функции для вызова из C#
  (export ""incCounter"" (func $incCounter))
  (export ""isPositive"" (func $isPositive))
  (export ""sumToN"" (func $sumToN))
  (export ""store"" (func $store))
  (export ""load"" (func $load))
  (export ""readAndLog"" (func $readAndLog))
)";

            // Компилируем модуль с расширенными возможностями
            using var moduleAdv = Module.FromText(engine, "advanced_module", watAdvanced);

            // Создаём хранилище
            using var storeAdv = new Store(engine);

            // Определяем импортируемую функцию "log" на стороне C#,
            // которая принимает int и выводит его в консоль
            var logAction = Function.FromCallback<int>(storeAdv, (int value) =>
            {
                Console.WriteLine($"[Wasm log] Значение из памяти: {value}");
            });

            // Инстанцируем модуль, передавая объект импорта с функцией "log" в пространстве "env"
            var linker = new Linker(engine);
            linker.Define("env", "log", logAction);
            var instanceAdv = linker.Instantiate(storeAdv, moduleAdv);

            // --- Демонстрация глобальной переменной ---
            var incCounter = instanceAdv.GetFunction<int>("incCounter");
            Console.WriteLine($"\nГлобальный счётчик после 1-го вызова: {incCounter()}");
            Console.WriteLine($"Глобальный счётчик после 2-го вызова: {incCounter()}");

            // --- Условная логика ---
            var isPositive = instanceAdv.GetFunction<int, int>("isPositive");
            Console.WriteLine($"\nisPositive(-5) = {isPositive(-5)}");
            Console.WriteLine($"isPositive(42) = {isPositive(42)}");

            // --- Цикл ---
            var sumToN = instanceAdv.GetFunction<int, int>("sumToN");
            int n = 10;
            Console.WriteLine($"\nСумма от 1 до {n} = {sumToN(n)}");

            // --- Работа с памятью ---
            var storeFunc = instanceAdv.GetFunction<int, object>("store");
            var loadFunc = instanceAdv.GetFunction<int>("load");
            // Получаем экспортированную память для прямого доступа из C# (для демонстрации сегментов и массивов)
            var memory = instanceAdv.GetMemory("mem");
            // Записываем число 99 через Wasm-функцию store
            storeFunc(99);
            // Читаем через Wasm-функцию load
            Console.WriteLine($"\nЧтение из памяти через load: {loadFunc()}");
            // Прямое чтение из памяти через C# (через буфер)
            var span = memory.GetSpan<byte>(0, (int)memory.GetLength());
            // Преобразуем первые 4 байта в Int32
            int directRead = BitConverter.ToInt32(span.Slice(0, 4));
            Console.WriteLine($"Прямое чтение из памяти C#: {directRead}");

            // --- Вызов импортированной функции log из Wasm ---
            var readAndLog = instanceAdv.GetFunction("readAndLog");
            Console.WriteLine("\nВызов readAndLog (Wasm вызывает импортированную функцию log):");
            readAndLog?.Invoke();

            Console.WriteLine("\n=== Демонстрация завершена. Нажмите любую клавишу... ===");
            Console.ReadKey();
        }
    }
}