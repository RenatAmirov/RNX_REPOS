def func1(x):
    def func2():
        print(x)
    return func2

f1 = func1(10)
f2 = func1(99)
f1()                 # Выведет: 10
f2()                 # Выведет: 99
