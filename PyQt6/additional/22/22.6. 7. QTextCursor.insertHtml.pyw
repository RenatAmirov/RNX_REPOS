from PyQt6 import QtWidgets
import sys

def on_clicked():
    textEdit.setFocus()
    cur = textEdit.textCursor()
    cur.beginEditBlock()              # Начало блока
    cur.insertHtml("<b>вставленный фрагмент 1</b>")
    cur.insertHtml("""<span style="color: red;"> вставленный фрагмент 2</span>""")
    cur.endEditBlock()                # Конец блока
    textEdit.setTextCursor(cur)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextCursor")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setHtml("<p>Блок 1</p><p>Блок 2</p>")
button = QtWidgets.QPushButton("Вставить текст")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
