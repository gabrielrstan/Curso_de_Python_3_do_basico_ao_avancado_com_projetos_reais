# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
# import os
# from itertools import count

# caminho = os.path.join('/home', 'stanzione', 'Aulas',
#                        'Curso_de_Python_3_do_basico_ao_avancado_com_projetos_reais',
#                        'Secao5')
# counter = count()

# for root, dirs, files in os.walk(caminho):
#     the_counter = next(counter)
#     print(the_counter, 'Pasta atual', root)

#     for dir_ in dirs:
#         print('  ', the_counter, 'Dir', dir_)

#     for file_ in files:
#         print('  ', the_counter, 'FILE', file_)
