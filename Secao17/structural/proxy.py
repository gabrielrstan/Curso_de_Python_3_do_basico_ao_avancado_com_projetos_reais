"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como o proxies são usados,
nós os classificamos como:

- Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização.
- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos.
- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão.
- Proxy inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from time import sleep
from typing import Dict, List


class IUser(ABC):
    first_name: str
    last_name: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]: ...

    @abstractmethod
    def get_all_user_data(self) -> Dict: ...


class RealUser(IUser):
    def __init__(self, first_name: str, last_name: str) -> None:
        sleep(2)
        self.first_name = first_name
        self.last_name = last_name

    def get_addresses(self) -> List[Dict]:
        sleep(2)
        return [
            {'rua': 'Av. Brasil', 'numero': 500}
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2)
        return {
            'cpf': '123.562.335-80',
            'rg': '23451023-5'
        }


class UserProxy(IUser):
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

        self._real_user: RealUser
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.first_name, self.last_name)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == '__main__':
    gabriel = UserProxy('Gabriel', 'Stanzione')

    print(gabriel.first_name)
    print(gabriel.last_name)
    print(gabriel.get_addresses())
    print(gabriel.get_all_user_data())

    print('CACHED DATA')
    for i in range(50):
        print(gabriel.get_addresses())
        print(gabriel.get_all_user_data())
        print("---")
