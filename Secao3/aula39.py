'''
Iterando strings com while
'''
nome = 'Gabriel Stanzione'
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
i = 0
while i < tamanho_nome:
    nova_string += '*' + nome[i]
    i += 1
nova_string += '*'
print(nova_string) 