from pathlib import Path
# from shutil import rmtree
caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

# ideias = caminho_arquivo.parent / 'ideias'
# print(ideias)

# arquivo = Path.home() / 'Área de trabalho' / 'arquivo.txt'
# arquivo.touch()
# arquivo.write_text('Olá Mundo')
# print(arquivo.read_text())
# arquivo.unlink()
# print(arquivo)
# ***
# caminho_arquivo = Path.home() / 'Área de trabalho' / 'arquivo.txt'
# caminho_arquivo.write_text('')
# with caminho_arquivo.open('a+') as file:
#     file.write('Uma linha\n')
#     file.write('Outra linha\n')

# print(caminho_arquivo.read_text())
# ***
caminho_arquivo = Path.home() / 'Área de trabalho' / 'arquivo.txt'
caminho_arquivo.touch()
caminho_arquivo.write_text('Olá Mundo')
caminho_arquivo.unlink()

caminho_pasta = Path.home() / 'Área de trabalho' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('😀')

mais_arquivo = caminho_pasta / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('😀')

# caminho_pasta.rmdir()

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá mundo\n')
        text_file.write(f'file_{i}.txt')

# rmtree(caminho_pasta)


# def rmtree(root=Path, remove_root=True):
#     for file in root.glob('*'):
#         if file.is_dir():
#             print('DIR: ', file)
#             rmtree(file, False)
#             file.rmdir()
#         else:
#             print('FILE: ', file)
#             file.unlink()

#     if remove_root:
#         root.rmdir()


# rmtree(caminho_pasta)
