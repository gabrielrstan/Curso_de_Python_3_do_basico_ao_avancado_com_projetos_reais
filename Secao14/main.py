# https://docs.python.org/3/library/doctest.html
# https://docs.python.org/3/library/unittest.html
# https://github.com/luizomf/python-tests

from calculadora import soma

# print(soma(10, 20))
# print(soma(-10, 20))
# print(soma(1.5, 2.5))
# print(soma('10', 10))

# try:
#     print(soma('10', 10))
# except TypeError as e:
#     print('Conta invalida')
#     print(e)

try:
    print(soma('10', 10))
except AssertionError as e:
    print(f'Conta invalida {e}')
