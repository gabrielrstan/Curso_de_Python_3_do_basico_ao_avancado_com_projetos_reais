# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
import copy

print(*produtos, sep='\n')
print()

novos_produtos = [{**produto, 'preco': produto['preco'] * 1.1}
			for produto in copy.deepcopy(produtos)]

# novos_produtos = copy.deepcopy(produtos)
print(*novos_produtos, sep='\n')
print()

produtos = sorted(produtos, key=lambda item: item['nome'], reverse=True)
print(*produtos, sep='\n')
print()

produtos_ordenados_por_nome = copy.deepcopy(
	sorted(produtos, key=lambda item: item['nome']))

print(*produtos_ordenados_por_nome, sep='\n')
print()

produtos = copy.deepcopy(
	sorted(produtos, key=lambda item: item['preco']))

produtos_ordenados_por_preco = produtos
print(*produtos_ordenados_por_preco, sep='\n')

