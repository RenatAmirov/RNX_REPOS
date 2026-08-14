from enum import Enum
class Frameworks3(Enum):
    LARAVEL = "Laravel"
    DJANGO = "Django"
    EXPRESS = "Express"
    RAILS = "Ruby on Rails"

    # Обычные методы. Вызываются у элемента перечисления.
    def describe(self):
        return self.name, self.value
    def __str__(self):
        return str(__class__.__name__) + "." + self.name + ": " + \
        self.value

    # Статический метод.  Вызывается у самого класса перечисления.
    @classmethod
    def getmostpopular(cls):
        return cls.LARAVEL
