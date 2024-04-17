"""
Command tem intenção de encapsular uma solicitação como
um objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registro (log) de solicitações e suportar
operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final).
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Light:
    def __init__(self, name: str, room_name: str) -> None:
        self._name = name
        self._room_name = room_name
        self.color = 'Default Color'

    def on(self) -> None:
        print(f'{self._name} in {self._room_name} is now ON')

    def off(self) -> None:
        print(f'{self._name} in {self._room_name} is now OFF')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'{self._name} in {self._room_name} is now {self.color}')


class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None: ...

    @abstractmethod
    def undo(self) -> None: ...


class LightOnCommand(ICommand):
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.on()

    def undo(self) -> None:
        self._light.off()


class LightChangeColor(ICommand):
    def __init__(self, light: Light, color: str) -> None:
        self._light = light
        self.color = color
        self._old_color = self._light.color

    def execute(self) -> None:
        self._old_color = self._light.color
        self._light.change_color(self.color)

    def undo(self) -> None:
        self._light.change_color(self._old_color)


class RemoteController:
    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_pressed(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name, 'execute'))

    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, 'undo'))

    def global_undo(self) -> None:
        if not self._undos:
            print('Nothing to undo')
            return None

        button_name, action = self._undos[-1]

        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        self._undos.pop()


if __name__ == '__main__':
    bedroom_light = Light('Luz do quarto', 'Quarto Gabriel')
    bathroom_light = Light('Luz do banheiro', 'Banheiro Gabriel')

    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)

    bedroom_light_red = LightChangeColor(bedroom_light, 'Red')
    bedroom_light_green = LightChangeColor(bedroom_light, 'Green')

    remote = RemoteController()

    remote.button_add_command('first_button', bedroom_light_on)
    remote.button_add_command('second_button', bathroom_light_on)
    remote.button_add_command('third_button', bedroom_light_red)
    remote.button_add_command('fourth_button', bedroom_light_green)

    remote.button_pressed('first_button')
    remote.button_undo('first_button')
    remote.button_pressed('second_button')
    remote.button_undo('second_button')
    remote.button_pressed('third_button')
    remote.button_undo('third_button')
    remote.button_pressed('fourth_button')
    remote.button_undo('fourth_button')
    remote.button_pressed('fourth_button')
    remote.button_pressed('third_button')
    remote.button_undo('third_button')
    print()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
