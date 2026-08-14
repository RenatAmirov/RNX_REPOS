import sys
tmp_in = sys.stdin                  # Сохраняем ссылку на поток stdin
f = open(r"c:\book\file.txt", "r")  # Открываем файл на чтение
sys.stdin = f                       # Перенаправляем ввод
while True:
    try:
        line = input()              # Считываем строку из файла
        print(line)                 # Выводим строку
    except EOFError:                # Если достигнут конец файла,
        break                       # выходим из цикла
sys.stdin = tmp_in                  # Восстанавливаем стандартный ввод
f.close()                           # Закрываем файл
input()
