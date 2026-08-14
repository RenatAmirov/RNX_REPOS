class Class1:         # Базовый класс
    def func1(self):
        print("Метод func1() класса Class1")
    def func2(self):
        print("Метод func2() класса Class1")

class Class2(Class1): # Производный класс Class2 наследует класс Class1
    def func2(self):
        print("Метод func2() класса Class2 перекрыл метод класса Class1")
    def func3(self):
        print("Метод func3() класса Class2")

c1 = Class1()        # Создаем объект класса Class1
c2 = Class2()        # Создаем объект класса Class2
c2.func1()           # Выведет: Метод func1() класса Class1
c1.func2()           # Выведет: Метод func2() класса Class1
c2.func2()  # Выведет: Метод func2() класса Class2 перекрыл метод класса Class1
c2.func3()           # Выведет: Метод func3() класса Class2
