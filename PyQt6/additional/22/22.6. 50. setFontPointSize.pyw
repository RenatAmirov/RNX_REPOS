from PyQt6 import QtWidgets
import sys

def on_clicked():
    textEdit.setFontPointSize(12)
    print(textEdit.fontPointSize())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setFontPointSize(30)
textEdit.setPlainText("Значение по умолчанию")
button = QtWidgets.QPushButton("Изменить размер шрифта")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
