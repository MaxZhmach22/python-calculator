from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
app = QtWidgets.QApplication([])
window = loader.load('./gui/gui.ui', None)


line_edit = window.findChild(QtWidgets.QLineEdit, 'lineEdit')
if line_edit is not None:
    line_edit.setText('Hello, World!')
else:
    print("QLineEdit с именем 'lineEdit' не найден")


def press_button():
    window.findChild(QtWidgets.QLineEdit, 'lineEdit').setText('Button clicked')


button = window.findChild(QtWidgets.QPushButton, 'pushButton_10')
button.clicked.connect(press_button)


window.show()
app.exec()
