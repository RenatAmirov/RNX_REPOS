from PyQt6 import QtCore, QtWidgets
import sys

def on_mypaste():
    textEdit.insertPlainText("мой текст")

class MyTextEdit(QtWidgets.QTextEdit):
    def __init__(self, text, parent=None):
        QtWidgets.QTextEdit.__init__(self, text, parent)

    def contextMenuEvent(self, e):
        menu = self.createStandardContextMenu()
        menu.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose)
        menu.addSeparator()
        menu.addAction("Новый пункт", on_mypaste, "Ctrl+M")
        menu.exec(e.globalPos())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = MyTextEdit("Значение по умолчанию")
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
window.setLayout(box)
window.show()
sys.exit(app.exec())
