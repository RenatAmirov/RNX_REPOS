from abc import ABC, abstractmethod
class MyClass(ABC):
    @staticmethod
    @abstractmethod
    def static_func(self, x):     # Абстрактный статический метод
        pass

    @classmethod
    @abstractmethod
    def class_func(self, x):      # Абстрактный метод класса
        pass
