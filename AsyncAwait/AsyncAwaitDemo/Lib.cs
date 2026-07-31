using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AsyncAwaitDemo
{
    internal class Lib
    {
        public void Method()
        {
            Task task = DoSomethingAsync();
        }

        async Task DoSomethingAsync()
        {
            int value = 13;
            // Асинхронно ожидать 1 секунду.
            await Task.Delay(TimeSpan.FromSeconds(10));
            value *= 2;
            Console.WriteLine(value);
            // Асинхронно ожидать 1 секунду.
            await Task.Delay(TimeSpan.FromSeconds(10));
            Console.WriteLine(value);
        }

    }
}
