"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID
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


class VeiculoFactory:
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

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

    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()


if __name__ == '__main__':
    carros_disponiveis = ['Luxo', 'Popular', 'Moto', 'Moto_Luxo']

    for i in range(10):
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.buscar_cliente()
