"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome? ')
    print('O seu nome é {}'.format(nome))

    if nome.lower() == 'sair':
        break

print('Acabou')