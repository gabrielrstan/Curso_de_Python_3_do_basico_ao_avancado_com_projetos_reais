"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self): ...

    def base_class_method(self):
        print("Base class method from abstract class")

    @abstractmethod
    def operation1(self): ...

    @abstractmethod
    def operation2(self): ...


class ConcreteClass1(Abstract):
    def hook(self):
        print("Hook from concrete class 1")

    def operation1(self):
        print("Operation 1 concluded")

    def operation2(self):
        print("Operation 2 concluded")


class ConcreteClass2(Abstract):
    def operation1(self):
        print("Operation 1 concluded in another way")

    def operation2(self):
        print("Operation 2 concluded in another way")


if __name__ == "__main__":
    c1 = ConcreteClass1()
    c1.template_method()
    print()
    c2 = ConcreteClass2()
    c2.template_method()
