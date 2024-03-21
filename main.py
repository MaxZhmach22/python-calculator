from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from oop.line_info import LineInfo
from oop.line_info import ButtonsInfo
from oop.button_click_handler import ButtonClickHandler


loader = QUiLoader()
app = QtWidgets.QApplication([])
window = loader.load('./gui/gui.ui', None)

line = LineInfo(window)
buttons_info = ButtonsInfo(window)
buttons_click_handler = ButtonClickHandler(buttons_info, line)


window.show()
app.exec()
