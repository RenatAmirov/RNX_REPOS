class Class1:
    def __init__(self):
        print("Конструктор базового класса")
    def func1(self):
        print("Метод func1() класса Class1")
    def func2(self):
        print("Метод func2() класса Class1")

class Class2(Class1):
    def __init__(self):
        print("Конструктор производного класса")
        Class1.__init__(self) # Вызываем конструктор базового класса
    def func1(self):
        print("Метод func1() класса Class2")
        super().func1()       # Вызываем метод базового класса
    def func2(self):
        print("Метод func2() класса Class2")
        super(Class2, self).func2()       # Вызываем метод базового класса

c = Class2()                  # Создаем объект класса Class2
c.func1()                     # Вызываем метод func1()
c.func2()                     # Вызываем метод func2()
