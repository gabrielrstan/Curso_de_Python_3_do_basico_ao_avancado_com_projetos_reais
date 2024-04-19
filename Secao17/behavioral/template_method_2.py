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


class Pizza(ABC):
    def prepare(self) -> None:
        self.hook_before_add_ingredients()
        self.add_ingredients()
        self.hook_after_add_ingredients()
        self.cook()
        self.cut()
        self.serve()

    def hook_before_add_ingredients(self) -> None: ...
    def hook_after_add_ingredients(self) -> None: ...

    def cut(self) -> None:
        print(f"{self.__class__.__name__} - Cutting the pizza")

    def serve(self) -> None:
        print(f"{self.__class__.__name__} - Serving the pizza")

    @abstractmethod
    def add_ingredients(self) -> None: ...

    @abstractmethod
    def cook(self) -> None: ...


class PortuguesePizza(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print(f'{self.__class__.__name__} - Washing ingredients before adding')

    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__} - Adding ingredients - ham, cheese, '
              f'onions, eggs and olives')

    def cook(self) -> None:
        print(f'{self.__class__.__name__} - Cooked for 45 minutes on the wood '
              f'stove')


class PepperoniPizza(Pizza):
    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__} - Adding ingredients - pepperoni and'
              ' cheese ')

    def cook(self) -> None:
        print(f'{self.__class__.__name__} - Cooked for 30 minutes on the wood '
              f'stove')


if __name__ == '__main__':
    por = PortuguesePizza()
    por.prepare()
    pep = PepperoniPizza()
    pep.prepare()
