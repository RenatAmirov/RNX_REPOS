from PyQt6 import QtWidgets
import sys

def on_clicked():
    print(lcd.value())
    print(lcd.intValue())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLCDNumber")
window.resize(300, 150)
lcd = QtWidgets.QLCDNumber(9)
lcd.display(123456789)
button = QtWidgets.QPushButton("Вывести значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(lcd)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
