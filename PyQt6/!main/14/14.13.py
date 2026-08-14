class MyError(Exception):
    def __init__(self, value):
        self.msg = value
    def __str__(self):
        return self.msg

# Обработка пользовательского исключения
try:
    raise MyError("Описание исключения")
except MyError as err:
    print(err)        # Вызывается метод __str__()
    print(err.msg)    # Обращение к атрибуту класса
# Повторно генерируем исключение
raise MyError("Описание исключения")
