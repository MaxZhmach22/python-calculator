from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
app = QtWidgets.QApplication([])
window = loader.load('./gui/gui.ui', None)
window.show()
app.exec()
