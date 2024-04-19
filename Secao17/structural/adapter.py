"""
Adapter é um padrão de projeto estrutural que
tem a intenção de permitir que duas classes
que seriam incompatíveis trabalhem em conjunto
através de um "adaptador".
"""
from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self) -> None: ...

    @abstractmethod
    def down(self) -> None: ...

    @abstractmethod
    def left(self) -> None: ...

    @abstractmethod
    def right(self) -> None: ...


class Control(IControl):
    def top(self) -> None:
        print("Top")

    def down(self) -> None:
        print("Down")

    def left(self) -> None:
        print("Left")

    def right(self) -> None:
        print("Right")


class NewControl:
    def move_top(self) -> None:
        print(f"{self.__class__.__name__}: Top")

    def move_down(self) -> None:
        print(f"{self.__class__.__name__}: Down")

    def move_left(self) -> None:
        print(f"{self.__class__.__name__}: Left")

    def move_right(self) -> None:
        print(f"{self.__class__.__name__}: Right")


class ControlAdapter:
    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        self.new_control.move_top()

    def down(self) -> None:
        self.new_control.move_down()

    def left(self) -> None:
        self.new_control.move_left()

    def right(self) -> None:
        self.new_control.move_right()


class ControlAdapter2(Control, NewControl):
    def top(self) -> None:
        self.move_top()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()

    def right(self) -> None:
        self.move_right()


if __name__ == "__main__":
    control2 = NewControl()
    control_object = ControlAdapter(control2)

    control_object.top()
    control_object.down()
    control_object.left()
    control_object.right()

    control_class = ControlAdapter2()

    control_class.top()
    control_class.down()
    control_class.left()
    control_class.right()
