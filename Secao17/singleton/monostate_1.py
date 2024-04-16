"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    _state = {
        'x': 10,
        'y': 20,
        'z': 30,
        'w': 40,
    }

    def __init__(self, name=None, surname=None) -> None:
        self.__dict__ = self._state
        self.x = self._state['x']

        if name is not None:
            self.name = name

        if surname is not None:
            self.surname = surname


if __name__ == '__main__':
    m1 = MonoStateSimple('Gabriel', 'Stanzione')
    m2 = MonoStateSimple()
    print(m1)
    print(m2)
    m1.x = 5
    print(m1)
    print(m2)
