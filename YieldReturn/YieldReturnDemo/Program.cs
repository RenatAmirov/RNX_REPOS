using System;
using System.Collections.Generic;

//foreach (int fib in Fibs(6))
//    Console.Write(fib + " ");
// Вывод: 1 1 2 3 5 8

//IEnumerable<int> Fibs(int fibCount)
//{
//    for (int i = 0, prevFib = 1, curFib = 1; i < fibCount; i++)
//    {
//        yield return prevFib;   // ← волшебство здесь
//        int newFib = prevFib + curFib;
//        prevFib = curFib;
//        curFib = newFib;
//    }
//}

await foreach (int ch in GenerateAsync())
    Console.Write(ch + " ");


async IAsyncEnumerable<int> GenerateAsync()
{
    for (int i = 0; i < 10; i++)
    {
        await Task.Delay(100);
        yield return i;
    }
}