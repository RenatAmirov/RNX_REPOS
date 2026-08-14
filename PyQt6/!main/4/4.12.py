print("Введите слово 'stop' для получения результата")
summa = 0
while True:
    x = input("Введите число: ")
    if x == "stop":
        break                      # Выход из цикла
    x = int(x)                     # Преобразуем строку в число
    summa += x
print("Сумма чисел равна:", summa)
input()
