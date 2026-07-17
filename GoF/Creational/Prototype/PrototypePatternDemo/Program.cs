using System;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary; // Для бинарной сериализации

// Паттерн Прототип (Prototype)
// Позволяет создавать новые объекты путём клонирования существующего экземпляра.
// В примере показаны два способа клонирования: поверхностное (MemberwiseClone) и глубокое (через сериализацию).

namespace PrototypePatternDemo
{
    // Класс, представляющий адрес (ссылочный тип).
    // Помечаем атрибутом [Serializable] для возможности бинарной сериализации.
    [Serializable]
    public class Address
    {
        public string City { get; set; }
        public string Street { get; set; }

        public Address(string city, string street)
        {
            City = city;
            Street = street;
        }

        // Переопределяем ToString для удобного вывода на экран.
        public override string ToString()
        {
            return $"{City}, {Street}";
        }
    }

    // Класс, реализующий прототип.
    // Содержит как значимые поля (int, string), так и ссылочное поле (Address).
    [Serializable] // Нужно для глубокого клонирования.
    public class Person
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public Address Address { get; set; }

        public Person(int id, string name, Address address)
        {
            Id = id;
            Name = name;
            Address = address;
        }

        // ---- Поверхностное копирование ----
        // Используем встроенный метод MemberwiseClone().
        // Он копирует значимые типы (Id, Name) и копирует ссылку на объект Address,
        // поэтому оригинал и клон будут ссылаться на один и тот же объект Address.
        public Person ShallowClone()
        {
            // MemberwiseClone() возвращает object, приводим к Person.
            return (Person)this.MemberwiseClone();
        }

        // ---- Глубокое копирование через бинарную сериализацию ----
        // Создаёт полностью независимую копию объекта, включая все вложенные объекты.
        public Person DeepClone()
        {
            // Проверяем, что объект помечен как [Serializable].
            if (!this.GetType().IsSerializable)
                throw new InvalidOperationException("Объект не сериализуем!");

            // Создаём BinaryFormatter и MemoryStream.
            BinaryFormatter formatter = new BinaryFormatter();
            using (MemoryStream stream = new MemoryStream())
            {
                // Сериализуем текущий объект в поток.
                formatter.Serialize(stream, this);
                // Перемещаем позицию в начало потока.
                stream.Seek(0, SeekOrigin.Begin);
                // Десериализуем обратно в объект и приводим к типу Person.
                return (Person)formatter.Deserialize(stream);
            }
        }

        // Переопределяем ToString для наглядного вывода.
        public override string ToString()
        {
            return $"Id: {Id}, Name: {Name}, Address: {Address}";
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Паттерн Прототип (Prototype) ===\n");

            // Создаём исходный объект (прототип).
            Person original = new Person(1, "Иван Петров", new Address("Москва", "Тверская ул., д. 1"));

            Console.WriteLine("Исходный объект (оригинал):");
            Console.WriteLine(original);
            Console.WriteLine();

            // ---- 1. Поверхностное клонирование ----
            Person shallowClone = original.ShallowClone();
            Console.WriteLine("Поверхностная копия (ShallowClone):");
            Console.WriteLine(shallowClone);
            Console.WriteLine();

            // Меняем адрес у поверхностной копии.
            // Так как адрес копируется по ссылке, изменение отразится и на оригинале.
            shallowClone.Address.City = "Санкт-Петербург";
            shallowClone.Address.Street = "Невский пр., д. 10";

            Console.WriteLine("После изменения адреса у поверхностной копии:");
            Console.WriteLine("Оригинал: " + original);
            Console.WriteLine("Копия:    " + shallowClone);
            Console.WriteLine("Видно, что адрес изменился в обоих объектах (поверхностное копирование).");
            Console.WriteLine();

            // ---- 2. Глубокое клонирование ----
            // Создаём ещё один объект, чтобы показать глубокое копирование.
            Person original2 = new Person(2, "Мария Смирнова", new Address("Казань", "Кремлёвская ул., д. 5"));
            Person deepClone = original2.DeepClone();

            Console.WriteLine("Исходный объект для глубокого клонирования:");
            Console.WriteLine(original2);
            Console.WriteLine();

            // Меняем адрес у глубокой копии.
            deepClone.Address.City = "Екатеринбург";
            deepClone.Address.Street = "Ленина пр., д. 15";

            Console.WriteLine("После изменения адреса у глубокой копии:");
            Console.WriteLine("Оригинал: " + original2);
            Console.WriteLine("Копия:    " + deepClone);
            Console.WriteLine("Видно, что адрес изменился ТОЛЬКО у копии (глубокое копирование).");
            Console.WriteLine();

            Console.WriteLine("Нажмите любую клавишу для завершения...");
            Console.ReadKey();
        }
    }
}