from PyQt6 import QtWidgets
import sys

def on_clicked():
    lcd.display(123456)

def on_overflow():
    print("Значение не может быть отображено")
    lcd.display("ERROR")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLCDNumber")
window.resize(300, 150)
lcd = QtWidgets.QLCDNumber()
lcd.setDigitCount(5)
lcd.display(15)
lcd.overflow.connect(on_overflow)
button = QtWidgets.QPushButton("Задать значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(lcd)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
