"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Informe o seu nome: ')
idade = input('Informe a sua idade: ')

if nome != '' and idade != '':
#if nome and idade:
    print('O seu nome é {}'.format(nome))
    print('O seu nome invertido é {}'.format(nome[::-1]))
    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')
    print('Seu nome tem {} letras'.format(len(nome)))
    print('A primeira letra do seu nome é {}'.format(nome[0]))
    print('A ultima letra do seu nome é {}'.format(nome[-1]))
else:
    print("Desculpe, você deixou campos vazios.")