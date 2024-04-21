"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0, 10 , 20, 30, 40)],  # 2
]
# print(salas)
# print()
# print(salas[1])
# print()
# print(salas[1][0])
# print()
# print(salas[0][1])
# print()
# print(salas[2][2])
# print()
# print(salas[2][3][2])

for sala in salas:
    print("A sala é {}".format(sala))
    for aluno in sala:
        print(aluno)