namespace SlicesDemo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int[] numbers = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

            // срез через конструктор Span<T>
            Span<int> slice = new Span<int>(numbers, start: 2, length: 5); // элементы 2..7

            // или через метод AsSpan (более удобный)
            Span<int> slice2 = numbers.AsSpan(2, 5);

            slice[0] = 42; // повлияет на numbers[2]!
        }

    }
}
