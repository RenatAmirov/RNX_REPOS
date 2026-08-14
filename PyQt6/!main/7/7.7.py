import re
def repl(m):
    """ Функция для замены. m — объект Match """
    x = int(m.group(0))
    x += 10
    return "{0}".format(x)

p = re.compile(r"[0-9]+")
# Заменяем все вхождения
print(p.sub(repl, "2019, 2020, 2021, 2022"))
# Заменяем только первые два вхождения
print(p.sub(repl, "2019, 2020, 2021, 2022", 2))
input()
