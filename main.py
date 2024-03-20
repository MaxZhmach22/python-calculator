from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from oop.line_info import LineInfo
from oop.line_info import ButtonsInfo
from oop.ButtonsEnum import ButtonsEnum

loader = QUiLoader()
app = QtWidgets.QApplication([])
window = loader.load('./gui/gui.ui', None)

line = LineInfo(window)
buttons_info = ButtonsInfo(window)


def press_button(button: ButtonsEnum):
    line.get_line().setText(f'{button.name} Button clicked')


buttons_info.equals.clicked.connect(lambda: press_button(ButtonsEnum.equals))
buttons_info.plus.clicked.connect(lambda: press_button(ButtonsEnum.plus))



window.show()
app.exec()
