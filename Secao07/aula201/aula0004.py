# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys

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


def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar
menu = window.menuBar()
first_menu = menu.addMenu('Primeiro Menu')
first_action = first_menu.addAction('Primeira acão')
first_action.triggered.connect(lambda: slot_example(status_bar))

window.show()
app.exec()  # O loop da aplicação
