# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6
#  G a b r i e l
# -7-6-5-4-3-2-1
# nome = 'Gabriel'
# print(nome[1])
# print(nome[-6])
# print('iel' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('iel' not in nome)
# print('zero' not in nome)

nome = input('Digite o seu nome: ')
encontar = input('Digite o que deseja encontar: ')

if encontar in nome:
    print('{} está em {}'.format(encontar, nome))
else:    
    print('{} não está em {}'.format(encontar, nome))