# Problema dos parâmetros mutáveis em funções Python

def add_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = add_clientes('Luiz')
add_clientes('Joana', cliente1)
add_clientes('Fernado', cliente1)
cliente1.append("Edu")

cliente2 = add_clientes('Helena')
add_clientes('Maria', cliente2)

cliente3 = add_clientes('Moreira')
add_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
