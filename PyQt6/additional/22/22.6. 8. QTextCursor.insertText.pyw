from PyQt6 import QtWidgets
import sys

def on_clicked():
    textEdit.setFocus()
    cur = textEdit.textCursor()
    cur.beginEditBlock()              # Начало блока
    cur.insertText("Новый блок 1\n")
    cur.insertText("Новый блок 2\n")
    cur.endEditBlock()                # Конец блока
    cur.joinPreviousEditBlock()       # Продолжение предыдущего блока
    cur.insertText("Новый блок 3\n")
    cur.endEditBlock()                # Конец блока
    textEdit.setTextCursor(cur)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextCursor")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setPlainText("Блок 1\nБлок 2\nБлок 3\nБлок 4\nБлок 5")
button = QtWidgets.QPushButton("Вставить текст")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
