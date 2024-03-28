import sqlite3
from pathlib import Path
# https://www.sqlite.org/doclist.html
# https://www.techonthenet.com/sqlite/index.php

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read   Update Delete
# SQL -  INSERT SELECT UPDATE DELETE


# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}')

# DELETE mais cuidadoso
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name = "{TABLE_NAME}"')
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
# CUIDADO: sql injection
# cursor.execute(
#     f'INSERT INTO {TABLE_NAME}'
#     '(id, name, weight) '
#     'VALUES'
#     '(NULL, "Helena", 4), '
#     '(NULL, "Eduardo", 10)'
# )
# connection.commit()

# sql = (
#     f'INSERT INTO {TABLE_NAME}'
#     '(name, weight) '
#     'VALUES'
#     '(?, ?)'
# )

sql = (
    f'INSERT INTO {TABLE_NAME}'
    '(name, weight) '
    'VALUES'
    '(:name, :weight) '
)

# cursor.execute(sql, ['Joana', 4])
# cursor.executemany(
#     sql,
#     (
#         ('Joana', 4), ('Luiz', 5)
#     )
# )

cursor.execute(sql, {'name': 'No Name', 'weight': 3})
cursor.executemany(sql, (
    {'name': 'Miguel', 'weight': 3},
    {'name': 'Mario', 'weight': 2},
    {'name': 'Jose', 'weight': 6},
    {'name': 'Marcos', 'weight': 7},
))

connection.commit()


if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "1"'
    )
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="Qualquer", weight=67.89 '
        'WHERE id = "2"'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME} '
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()
