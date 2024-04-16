# uma_string: str = 'Um valor'
# um_inteiro: int = 0
# um_float: float = 0.0
# um_boolean: bool = False
# um_set: set = {1, 2, 3}
# uma_lista: list = []
# uma_tupla: tuple = 1, 2, 3
# um_dicionario: dict = {}


# def soma(x: int, y: int, z: float) -> float:
#     return x + y + z


# lista_inteiros: list[int] = [1, 2, 3, 4, 5]
# lista_string: list[str] = ['a', 'b', 'c', 'd', 'e']
# lista_tuplas: list[tuple] = [(1, "a"), (2, "b"), (3, "c")]
# lista_listas_int: list[list[int]] = [[1, 2], [3, 4]]

# um_dict: dict[str, int] = {
#     "A": 0,
#     "B": 1,
#     "C": 2,
#     "D": 3,
#     "E": 4,
#     "F": 5,
# }

# um_dict_de_listas: dict[str, list[int]] = {
#     "A": [1, 2],
#     "B": [3, 4],
#     "C": [5, 6],
#     "D": [7, 8],
#     "E": [9, 10],
#     "F": [11, 12],
# }

# um_set_de_inteiros: set[int] = {1, 2, 3, 4, 5, 6, 7}

# ListaInteiros = list[int]  # Type alias
# DictListaInteiros = dict[str, ListaInteiros]

# um_dict_de_listas: DictListaInteiros = {
#     "A": [1, 2],
#     "B": [3, 4],
#     "C": [5, 6],
#     "D": [7, 8],
#     "E": [9, 10],
#     "F": [11, 12],
# }

# string_e_inteiros: str | int = 1
# string_e_inteiros: str | int = "A"
# string_e_inteiros: str | int = 2
# lista: list[int | str] = [1, 2, 3, 'A', 'B', 'C']

# def soma(x: int, y: float | None = None) -> float:
#     if isinstance(y, float | int):
#         return x + y
#     return x + x

# from collections.abc import Callable

# SomaInteiros = Callable[[int, int], int]

# def executa(func: SomaInteiros, a: int, b: int) -> int:
#     return func(a, b)


# def soma(a: int, b: int) -> int:
#     return a + b


# executa(soma, 1, 2)

# from typing import TypeVar

# T = TypeVar('T')


# def get_item(list: list[T], index: int) -> T:
#     return list[index]


# list_int = get_item([1, 2, 3], 1)
# list_str = get_item(['a', 'b', 'c'], 1)  # str

# class Person:
#     def __init__(self, firstname: str, lastname: str) -> None:
#         self.nome: str = firstname
#         self.sobrenome: str = lastname

#     @property
#     def full_name(self):
#         return f'{self.nome} {self.sobrenome}'


# def say_my_name(person: Person) -> str:
#     return person.full_name


# print(say_my_name(Person('John', 'Smith')))
