from PyQt6 import QtCore, QtWidgets
import sys

def on_mypaste():
    lineEdit.insert("мой текст")

class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)

    def contextMenuEvent(self, e):
        menu = self.createStandardContextMenu()
        menu.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)
        menu.addSeparator()
        menu.addAction("Новый пункт", on_mypaste, "Ctrl+M")
        menu.exec(e.globalPos())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLineEdit")
window.resize(300, 50)
lineEdit = MyLineEdit()
box = QtWidgets.QVBoxLayout()
box.addWidget(lineEdit)
window.setLayout(box)
window.show()
sys.exit(app.exec())
