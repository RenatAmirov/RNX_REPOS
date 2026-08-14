from PyQt6 import QtWidgets
import sys

def on_clicked():
    print("Сигнал clicked")

def on_pressed():
    print("Сигнал pressed")

def on_released():
    print("Сигнал released")

def on_toggled(status):
    print("Сигнал toggled", status)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
button1 = QtWidgets.QPushButton("Обычная кнопка")
button2 = QtWidgets.QPushButton("Кнопка-переключатель")
button2.setCheckable(True)
button1.clicked.connect(on_clicked)
button1.pressed.connect(on_pressed)
button1.released.connect(on_released)
button2.toggled["bool"].connect(on_toggled)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
