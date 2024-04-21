"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
import time

lista = []

while True:
    print('Selecione a opção:')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao.lower() == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao.lower() == 'a':
        os.system('clear')
        indice = input('Escolha o indice para apagar: ')
        try:
            indice_int = int(indice)
            del lista[indice_int]
        except:
            print("Valor invalido")
    elif opcao.lower() == 'l':
        os.system('clear')
        if len(lista) == 0:
            print('Nada para listar')
        for indice, nome in enumerate(lista):
            print(indice, nome)

    else:
        print('Opção invalida')
