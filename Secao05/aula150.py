# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager


@contextmanager
def my_open(path, mode):
    try:
        print('Abrindo Arquivo')
        file = open(path, mode)
        yield file
    except Exception as e:
        print('Ocorreu errro', e)
    finally:
        print('Fechando Arquivo')
        file.close()


with my_open('./Secao5/aula150.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n', 11)
    file.write('Linha 3\n')
    print('WITH', file)
