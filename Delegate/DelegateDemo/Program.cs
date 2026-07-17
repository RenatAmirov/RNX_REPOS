using System;
using System.IO;

namespace DelegateDemo
{
    internal class Program
    {
        // 1. Объявляем делегат — он описывает метод, который принимает строку и ничего не возвращает
        public delegate void MessageHandler(string message);

        // 2. Методы, подходящие по сигнатуре
        static void PrintToConsole(string msg) => Console.WriteLine($"Console: {msg}");
        static void PrintToFile(string msg) => File.WriteAllText("log.txt", msg);

        // 3. Используем делегат
        static void Main()
        {
            MessageHandler handler = PrintToConsole; // кладём метод в конверт
            handler("Привет, мир!");                 // выполняем — выведет в консоль

            handler = PrintToFile;                   // меняем поведение
            handler("Запись в файл!");               // сохранит в файл
        }
    }
}
