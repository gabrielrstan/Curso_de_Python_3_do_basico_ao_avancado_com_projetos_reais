"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobrar  o numero que vc digitar: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print('O dobro de {} é {:.2f}'.format(numero_str, numero_float*2))

except:
    print('Isso não é um numero')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print('O dobro de {} é {:.2f}'.format(numero_str, numero_float*2))
# else:
#     print('Isso não é um numero')
