print("Введите слово 'stop' для получения результата")
summa = 0
while (x := input("Введите число: ")) != "stop":
    x = int(x)
    summa += x
print("Сумма чисел равна:", summa)
input()
