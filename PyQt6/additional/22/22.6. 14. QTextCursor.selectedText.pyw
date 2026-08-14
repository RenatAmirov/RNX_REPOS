from PyQt6 import QtWidgets
import sys

def on_clicked():
    textEdit.setFocus()
    cur = textEdit.textCursor()
    if cur.hasSelection():
        print(cur.selectedText().replace("\u2029", "\n"))
    else:
        print("Ничего не выделено")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextCursor")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setPlainText("Блок 1\nБлок 2\nБлок 3\nБлок 4\nБлок 5")
button = QtWidgets.QPushButton("Получить выделенный фрагмент")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
