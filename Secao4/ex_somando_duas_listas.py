"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
def adding(l1, l2):
	max_range = min(len(l1), len(l2))
	sum_list = []
	for i in range(max_range):
		sum_list.append(l1[i] + l2[i])
	return sum_list

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
adding(lista_a, lista_b)
print(adding(lista_a, lista_b))