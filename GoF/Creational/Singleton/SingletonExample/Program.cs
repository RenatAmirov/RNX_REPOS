using System;

namespace SingletonExample
{
    // 1. Класс Singleton – реализует паттерн "Одиночка".
    public class Singleton
    {
        // 2. Приватное статическое поле – хранит единственный экземпляр класса.
        private static Singleton _instance;

        // 3. Приватный конструктор – запрещает создание экземпляров через new.
        private Singleton()
        {
            // Для демонстрации выводим сообщение о создании объекта.
            Console.WriteLine(">>> Приватный конструктор вызван. Создан новый экземпляр.");
            // При инициализации можно задать какие-либо данные (например, текущее время).
            _creationTime = DateTime.Now;
        }

        // 4. Пример данных, хранящихся в объекте (демонстрация состояния).
        private DateTime _creationTime;

        // 5. Публичное свойство для доступа к данным (только для чтения).
        public DateTime CreationTime => _creationTime;

        // 6. Статический метод GetInstance – глобальная точка доступа к экземпляру.
        public static Singleton GetInstance()
        {
            // 7. Если экземпляр ещё не создан, создаём его (ленивая инициализация).
            if (_instance == null)
            {
                _instance = new Singleton();
            }
            // 8. Возвращаем единственный экземпляр.
            return _instance;
        }
    }

    // 9. Главный класс программы.
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Демонстрация паттерна Одиночка (Singleton) ===\n");

            // 10. Первый вызов GetInstance – создаёт новый экземпляр.
            Singleton s1 = Singleton.GetInstance();
            Console.WriteLine($"s1.CreationTime = {s1.CreationTime:T}");

            // 11. Второй вызов GetInstance – возвращает уже существующий экземпляр.
            Singleton s2 = Singleton.GetInstance();
            Console.WriteLine($"s2.CreationTime = {s2.CreationTime:T}");

            // 12. Проверяем, что s1 и s2 ссылаются на один и тот же объект.
            bool areSame = ReferenceEquals(s1, s2);
            Console.WriteLine($"\ns1 и s2 указывают на один объект? {areSame}");

            // 13. Дополнительно: вывод хеш-кодов (для наглядности).
            Console.WriteLine($"Хеш-код s1: {s1.GetHashCode()}");
            Console.WriteLine($"Хеш-код s2: {s2.GetHashCode()}");

            // 14. Попытка создать объект через new – вызовет ошибку компиляции,
            // так как конструктор приватный (раскомментируйте следующую строку, чтобы убедиться):
            // Singleton s3 = new Singleton(); // Ошибка CS0122: недоступен из-за уровня защиты.

            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();
        }
    }
}