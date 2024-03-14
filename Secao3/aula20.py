primeiro_valor = input('Digite uma valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print('O primeiro valor {} é maior que o segundo valor {}'.format(primeiro_valor, segundo_valor))
elif segundo_valor > primeiro_valor:
    print('O segundo valor {} é maior que o primeiro valor {}'.format(segundo_valor, primeiro_valor))
else:
    print('Ambos os valores são iguais')