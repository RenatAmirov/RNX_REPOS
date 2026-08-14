from PyQt6 import QtWidgets
import sys

def on_clicked_button1():
    print("Нажата кнопка 1")

def on_clicked_button2():
    print("Нажата кнопка 2")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QDialog()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
line = QtWidgets.QLineEdit()
button1 = QtWidgets.QPushButton("Обычная кнопка")
button2 = QtWidgets.QPushButton("Кнопка по умолчанию")
button1.clicked.connect(on_clicked_button1)
button2.pressed.connect(on_clicked_button2)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(line)
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
window.show()
button1.setAutoDefault(True)
button2.setAutoDefault(True)
button2.setDefault(False)
button2.setDefault(True)
sys.exit(app.exec())
