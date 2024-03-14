# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variáve

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def par_impar(x):
    return "Par" if x % 2 == 0 else 'Impar'

print(multiplica(5, 4, 3, 2, 1))
print(par_impar(50))