from PyQt6 import QtWidgets
import sys

def on_clicked():
    textEdit.setFocus()
    cur = textEdit.textCursor()
    print(cur.blockNumber())
    print(cur.block())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextCursor")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setPlainText("Блок 1\nБлок 2\nБлок 3\nБлок 4\nБлок 5")
button = QtWidgets.QPushButton("Получить блок, содержащий курсор")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
