# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self,):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


gol = Carro('Gol')
volkswagen = Fabricante('Volkswagen')
motor1_3 = Motor('Motor 1.3')
gol.fabricante = volkswagen
gol.motor = motor1_3

polo = Carro('Polo')
polo.fabricante = volkswagen
polo.motor = motor1_3

corsa = Carro('Corsa')
chevrolet = Fabricante('Chevrolet')
corsa.fabricante = chevrolet
corsa.motor = motor1_3

carros = [corsa, gol, polo]

for carro in carros:
    print(carro.fabricante.nome, carro.nome, carro.motor.nome)
