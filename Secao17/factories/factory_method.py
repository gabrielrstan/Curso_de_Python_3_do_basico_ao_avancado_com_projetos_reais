"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod
from random import choice


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: ...


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo está buscando o cliente")


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de popular está buscando o cliente")


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto de luxo está buscando o cliente")


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto popular está buscando o cliente")


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: ...

    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == "Luxo":
            return CarroLuxo()
        elif tipo == "Popular":
            return CarroPopular()
        elif tipo == "Moto":
            return MotoPopular()
        elif tipo == 'Moto_Luxo':
            return MotoLuxo()
        else:
            raise ValueError('Tipo de veículo não existe')


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == "Popular":
            return CarroPopular()
        else:
            raise ValueError('Tipo de veículo não existe')


if __name__ == '__main__':
    veiculos_disponiveis_zona_norte = ['Luxo', 'Popular', 'Moto', 'Moto_Luxo']
    veiculos_disponiveis_zona_sul = ['Popular']

    print('ZONA NORTE')
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(
            choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print()

    print('ZONA SUL')
    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(
            choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()
