import sys
import qdarktheme  # type:ignore

from buttons import ButtonsGrid
from main_window import MainWindow
from display import Display
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
# from styles import setupTheme
# https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/
# https://pyinstaller.org/en/stable/
# pyinstaller --name="Calculadora" --noconfirm --onefile --add-data='..files/:files/' --icon='..files/icon.png' --noconsole --clean --log-level=WARN main.py

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    # setupTheme()
    dark_stylesheet = qdarktheme.load_stylesheet('dark')
    window = MainWindow()

    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua conta')
    window.addWigdetToVLayout(info)

    # Display
    display = Display()
    window.addWigdetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    app.setStyleSheet(dark_stylesheet)
    window.adjustFixedSize()
    window.show()
    app.exec()
