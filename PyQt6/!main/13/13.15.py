class MyClass:
    def get_var(self):        # Геттер
        return self.__var
    def set_var(self, value): # Сеттер
        self.__var = value
    def del_var(self):        # Делетер
        del self.__var
    v = property(fget=get_var, fset=set_var, fdel=del_var, doc="Свойство")

c = MyClass()
c.v = 35                    # Вызывается геттер
print(c.v)                  # Вызывается сеттер
del c.v                     # Вызывается делетер
