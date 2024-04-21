"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print('{}'.format(variavel))
print('{: >10}.'.format(variavel))
print('{: ^10}'.format(variavel))
print(f'{1000.523265989562326598952:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')