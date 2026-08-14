def __getattr__(name):
    # При попытке обратиться к переменной c выдаем значение переменной d.
    # При обращении к другим переменным генерируем исключение
    if name == "c":
        return d
    else:
        raise AttributeError

def __dir__():
    return ("a", "b", "d")

a = 10
b = 20
d = 10000
