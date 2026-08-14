d = {"z": 3, "y": 2, "x": 1 }
k = list(d.keys())            # Получаем список ключей
k.sort()                      # Сортируем список ключей
for key in k:
    print("({0} => {1})".format(key, d[key]), end=" ")
# Выведет: (x => 1) (y => 2) (z => 3)
