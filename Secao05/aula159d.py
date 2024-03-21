# Valores padrão e field em dataclasses
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field, fields


@dataclass
class Pessoa:
    nome: str = field(
        default="Missing", repr=False)
    sobrenome: str = 'Not send'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa()
    print(fields(p1))
    print(p1)
