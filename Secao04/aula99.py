# from sys import path

# import aula99_package.modulo
# from aula99_package import modulo
# https://stackoverflow.com/questions/2386714/why-is-import-bad
# from aula99_package.modulo import * # Má pratica
# # from aula99_package.modulo import soma_do_modulo

# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(aula99_package.modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
# from aula99_package.modulo import soma_do_modulo, fala_oi

# print(__name__)
# fala_oi()

from aula99_package import soma_do_modulo, fala_oi

print(soma_do_modulo(5, 2))
fala_oi()