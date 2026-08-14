def func1(x):
    def func2():
        print(x)
    x = 30
    return func2

f1 = func1(10)
f2 = func1(99)
f1()                 # Выведет: 30
f2()                 # Выведет: 30
