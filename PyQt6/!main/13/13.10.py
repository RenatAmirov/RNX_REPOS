class MyClass:
    @staticmethod
    def func1(x, y):               # Статический метод
        return x + y
    def func2(self, x, y):         # Обычный метод
        return x + y
    def func3(self, x, y):
        return MyClass.func1(x, y) # Вызов статического метода из обычного

print(MyClass.func1(10, 20))       # Вызываем статический метод
c = MyClass()
print(c.func2(15, 6))              # Вызываем обычный метод
print(c.func1(50, 12))             # Вызываем статический метод через объект
print(c.func3(23, 5))              # Вызываем обычный метод,
                                   # вызывающий статический метод
