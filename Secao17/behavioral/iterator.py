"""
Iterator é um padrão comportamental que tem a
intenção de fornecer um meio de acessar,
sequencialmente, os elementos de um objeto
agregado sem expor sua representação subjacente.

- Uma coleção deve fornecer um meio de acessar
    seus elementos sem expor sua estrutura interna
- Uma coleção pode ter maneiras e percursos diferentes
    para expor seus elementos
- Você deve separar a complexidade dos algoritmos
    de iteração da coleção em si

A ideia principal do padrão é retirar a responsabilidade
de acesso e percurso de uma coleção, delegando tais
tarefas para um objeto iterador.
"""
from collections.abc import Iterable, Iterator
from typing import Any, List


class MyIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        super().__init__()
        self._collection = collection
        self._index = 0

    def next(self):
        try:
            return self.__next__
        except StopIteration:
            return None

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError as exc:
            raise StopIteration from exc


class ReverseIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        super().__init__()
        self._collection = collection
        self._index = -1

    def next(self):
        try:
            return self.__next__
        except StopIteration:
            return None

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError as exc:
            raise StopIteration from exc


class MyList(Iterable):
    def __init__(self) -> None:
        super().__init__()
        self._items: List[Any] = []
        self._my_iterator = MyIterator(self._items)

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


if __name__ == '__main__':
    my_list = MyList()
    my_list.add('Gabriel')
    my_list.add('Joanna')
    my_list.add('Jorge')
    print(my_list)
    print()
    for i in my_list:
        print(i)

    print()

    for i in my_list.reverse_iterator():
        print(i)
