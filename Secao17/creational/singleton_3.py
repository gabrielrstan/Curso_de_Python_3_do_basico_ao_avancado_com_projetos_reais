# class Meta(type):
#     def __call__(self, *args, **kwargs):
#         return super().__call__(*args, **kwargs)


# class Person(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls)

#     def __init__(self, name):
#         self.name = name

#     def __call__(self, x, y):
#         print("Call called", self.name, x + y)


# p1 = Person('Gabriel')
# p1(2, 9)
# print(p1.name)
from typing import Dict


class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.theme = 'DarkTheme'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.theme = 'LightTheme'
    print(as1.theme)

    as2 = AppSettings()
    as3 = AppSettings()
    print(as2.theme)
    print(as3.theme)
    print(as1 == as2)
    print(as1 == as3)
    print(as2 == as3)
