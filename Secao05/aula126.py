# Atributos de classe
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
# p1.nome = 'Eita'
# del p1.nome
# print(p1.idade)
# p1.__dict__['outra'] = 'outra'
# p1.__dict__['nome'] = 'eita'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.nome)
print(vars(p1))

dados = {'nome': 'Carol', 'idade': 35}
p2 = Pessoa(**dados)
print(vars(p2))
print(p2.nome)
