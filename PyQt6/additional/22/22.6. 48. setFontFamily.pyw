from PyQt6 import QtWidgets
import sys

def on_clicked():
    textEdit.setFontFamily("Courier New")
    print(textEdit.fontFamily())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setFontFamily("Tahoma")
textEdit.setPlainText("Значение по умолчанию")
button = QtWidgets.QPushButton("Изменить шрифт")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
