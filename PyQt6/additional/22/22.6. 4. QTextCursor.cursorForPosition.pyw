from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    textEdit.setFocus()
    cur = textEdit.cursorForPosition(QtCore.QPoint(100, 5))
    textEdit.setTextCursor(cur)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextCursor")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit("Значение по умолчанию")
button = QtWidgets.QPushButton("Установить курсор")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
