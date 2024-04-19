"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""
from __future__ import annotations

from abc import ABC, abstractmethod


class Order:
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        self.state.pending()
        print('Current state:', self.state)
        print()

    def approve(self) -> None:
        self.state.approve()
        print('Current state:', self.state)
        print()

    def reject(self) -> None:
        self.state.reject()
        print('Current state:', self.state)
        print()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: ...

    @abstractmethod
    def approve(self) -> None: ...

    @abstractmethod
    def reject(self) -> None: ...

    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPending(OrderState):
    def pending(self) -> None:
        print("Trying to execute pending")
        print("Payment already pending, cannot do anything")

    def approve(self) -> None:
        print("Trying to execute approve")
        self.order.state = PaymentAproved(self.order)
        print("Payment approved")

    def reject(self) -> None:
        print("Trying to execute reject")
        self.order.state = PaymentRejected(self.order)
        print("Payment rejected")


class PaymentAproved(OrderState):
    def pending(self) -> None:
        print("Trying to execute pending")
        self.order.state = PaymentPending(self.order)
        print('Payment pending')

    def approve(self) -> None:
        print("Trying to execute approve")
        print('Payment already approved, cannot do anything')

    def reject(self) -> None:
        print("Trying to execute reject")
        self.order.state = PaymentRejected(self.order)
        print('Payment rejected')


class PaymentRejected(OrderState):
    def pending(self) -> None:
        print("Trying to execute pending")
        print('Payment rejected, cannot do anything')

    def approve(self) -> None:
        print("Trying to execute approve")
        print('Payment rejected, cannot do anything')

    def reject(self) -> None:
        print("Trying to execute reject")
        print('Payment already rejected, cannot do anything')


if __name__ == '__main__':
    o = Order()
    o.pending()
    o.approve()
    o.pending()
    o.reject()
    o.pending()
    o.approve()
