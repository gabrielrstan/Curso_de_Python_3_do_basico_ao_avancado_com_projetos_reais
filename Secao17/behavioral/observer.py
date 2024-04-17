"""
O padrão Observer tem a intenção de
definir uma dependência de um-para-muitos entre
objetos, de maneira que quando um objeto muda de
estado, todo os seus dependentes são notificados
e atualizados automaticamente.

Um observer é um objeto que gostaria de ser
informado, um observable (subject) é a entidade
que gera as informações.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List


class IObservable(ABC):
    @property
    @abstractmethod
    def state(self): ...
    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: ...

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: ...

    @abstractmethod
    def notify_observers(self) -> None: ...


class WeatherStation(IObservable):
    def __init__(self):
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self) -> Dict:
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}
        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: ...


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self._name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self._name} o objeto {observable_name} acabou de ser '
              f'atualizado => {self.observable.state}')
        print()


class Notebook(IObserver):
    def __init__(self, observable: IObservable) -> None:
        self.observable = observable

    def show(self):
        state = self.observable.state
        print("Usando o notebook e realizando outras ações", state)
        print()

    def update(self) -> None:
        self.show()


if __name__ == '__main__':
    weather_station = WeatherStation()

    smartphone = Smartphone('iPhone', weather_station)
    another_smartphone = Smartphone('Xiaomi', weather_station)
    notebook = Notebook(weather_station)

    weather_station.add_observer(smartphone)
    weather_station.add_observer(another_smartphone)
    weather_station.add_observer(notebook)

    weather_station.state = {'temperature': 30}
    weather_station.state = {'temperature': 20}
    weather_station.state = {'humidity': 90}

    weather_station.remove_observer(smartphone)
    weather_station.reset_state()
