# Escopo da classe e de métodos da classe
class Animal:

    def __init__(self, nome):
        self.nome = nome

    def acao(self):
        return f'{self.nome} está executando uma ação'

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.acao())
# print(leao.comendo('carne'))
print(leao.executar('carne'))
