# O básico sobre Signal e Slots (eventos e documentação)
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget,
                               QGridLayout, QMainWindow)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela')

button1 = QPushButton('Texto do botão')
button1.setStyleSheet('font-size: 80px;')

button2 = QPushButton('Botão 2')
button2.setStyleSheet('font-size: 40px;')

button3 = QPushButton('Botão 3')
button3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button1, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
layout.addWidget(button3, 3, 1, 1, 2)


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O meu slot foi executado')
    return inner


@Slot()
def another_slot(checked):
    print('Esta marcado?', checked)


@Slot()
def third_slot(action):
    def inner():
        another_slot(action.isChecked())
    return inner


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar
menu = window.menuBar()
first_menu = menu.addMenu('Primeiro Menu')
first_action = first_menu.addAction('Primeira acão')
first_action.triggered.connect(slot_example(status_bar))

second_action = first_menu.addAction('Segunda acão')
second_action.setCheckable(True)
second_action.toggled.connect(another_slot)
second_action.hovered.connect(third_slot(second_action))

button1.clicked.connect(third_slot(second_action))

window.show()
app.exec()  # O loop da aplicação
