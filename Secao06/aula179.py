# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'

with open(CAMINHO_CSV, 'r', encoding='utf-8') as file:
    leitor = csv.DictReader(file)

    for linha in leitor:
        print(linha['Nome'], linha['Idade'], linha['Endereço'])

# with open(CAMINHO_CSV, 'r') as file:
#     leitor = csv.reader(file)

#     for linha in leitor:
#         print(linha)
