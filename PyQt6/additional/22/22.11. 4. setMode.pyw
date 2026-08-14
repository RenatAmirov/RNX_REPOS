from PyQt6 import QtWidgets
import sys
from functools import partial

def on_clicked():
    print(lcd.value())
    print(lcd.intValue())

def on_mode(mode):
    lcd.setMode(mode)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLCDNumber")
window.resize(300, 250)
lcd = QtWidgets.QLCDNumber(9)
lcd.display(255)
button = QtWidgets.QPushButton("Вывести значение")
button.clicked.connect(on_clicked)
button1 = QtWidgets.QPushButton("Двоичное значение")
button1.clicked.connect(partial(on_mode, QtWidgets.QLCDNumber.Mode.Bin))
button2 = QtWidgets.QPushButton("Восьмеричное значение")
button2.clicked.connect(partial(on_mode, QtWidgets.QLCDNumber.Mode.Oct))
button3 = QtWidgets.QPushButton("Десятичное значение")
button3.clicked.connect(partial(on_mode, QtWidgets.QLCDNumber.Mode.Dec))
button4 = QtWidgets.QPushButton("Шестнадцатеричное значение")
button4.clicked.connect(partial(on_mode, QtWidgets.QLCDNumber.Mode.Hex))
box = QtWidgets.QVBoxLayout()
box.addWidget(lcd)
box.addWidget(button)
box.addWidget(button1)
box.addWidget(button2)
box.addWidget(button3)
box.addWidget(button4)
window.setLayout(box)
window.show()
sys.exit(app.exec())
