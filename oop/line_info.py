from PySide6 import QtWidgets
from oop.buttons_enum import ButtonsEnum


class LineInfo:
    def __init__(self, window):
        self.__line = window.findChild(QtWidgets.QLineEdit, 'lineEdit')

    @property
    def line(self):
        return self.__line


class ButtonsInfo:
    def __init__(self, window):
        for button in ButtonsEnum:
            setattr(self, f'{button.name}', window.findChild(QtWidgets.QPushButton, button.value))
