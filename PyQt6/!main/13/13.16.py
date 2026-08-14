class MyClass:
    @property
    def v(self):                       # Геттер
        return self.__var
    @v.setter
    def v(self, value):                # Сеттер
        self.__var = value
    @v.deleter
    def v(self):                       # Делетер
        del self.__var

c = MyClass()
c.v = 35                               # Вызывается сеттер
print(c.v)                             # Вызывается геттер
del c.v                                # Вызывается делетер
