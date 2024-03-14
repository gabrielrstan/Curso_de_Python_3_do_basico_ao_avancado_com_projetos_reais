# Trabalhando com classes e herança no PySide6
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget,
                               QGridLayout, QMainWindow)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela')

        # Botão
        self.button1 = self.make_button('Texto do botão')
        self.button1.clicked.connect(self.second_action_checked)

        self.button2 = self.make_button('Botão 2')

        self.button3 = self.make_button('Botão 3')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.button1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.button2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.button3, 3, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        # menuBar
        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('Primeiro Menu')
        self.first_action = self.first_menu.addAction('Primeira acão')
        self.first_action.triggered.connect(self.change_status_bar_message)

        self.second_action = self.first_menu.addAction('Segunda acão')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.second_action_checked)
        self.second_action.hovered.connect(self.second_action_checked)

    @Slot()
    def change_status_bar_message(self):
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def second_action_checked(self):
        print('Esta marcado?', self.second_action.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 80px;')
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()  # O loop da aplicação
