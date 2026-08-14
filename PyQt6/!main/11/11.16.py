def deco(f):
    print("Вызвана функция func()")
    return f

def func(x):
    return "x = {0}".format(x)

# Вызываем функцию func() через функцию deco()
print(deco(func)(10))
