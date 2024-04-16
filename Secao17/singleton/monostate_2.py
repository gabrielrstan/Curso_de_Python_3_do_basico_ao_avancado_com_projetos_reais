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


class MonoState(StringReprMixin):
    _state = {
        'x': 10,
        'y': 20,
        'z': 30,
        'w': 40,
    }

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, name=None, surname=None) -> None:

        if name is not None:
            self.name = name

        if surname is not None:
            self.surname = surname


class A(MonoState):
    ...


if __name__ == '__main__':
    m1 = MonoState('Gabriel')
    m2 = A(surname='Stanzione')
    print(m1)
    print(m2)
