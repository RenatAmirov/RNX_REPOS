from PyQt6 import QtWidgets
import sys

def on_clicked():
    textEdit.setFontUnderline(True)
    print(textEdit.fontUnderline())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setFontUnderline(False)
textEdit.setPlainText("Значение по умолчанию")
button = QtWidgets.QPushButton("Сделать текст подчеркнутым")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
