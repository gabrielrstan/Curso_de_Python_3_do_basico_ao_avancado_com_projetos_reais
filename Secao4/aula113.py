# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]
# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]

# def funcao_do_reduce(acumulador, produto):
# 	# print('acumulador', acumulador)
# 	# print("produto", produto)
# 	return acumulador + produto['preco']

# total = 0
# for p in produtos:
# 	total += p['preco']

# print(total)

# print(sum([p['preco'] for p in produtos]))

# total = reduce(funcao_do_reduce, produtos, 0)
total = reduce(lambda ac, p: ac + p['preco'], produtos, 0)
print('O total é:', total)