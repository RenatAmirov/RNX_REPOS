from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    print("Кнопка нажата")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 80)
button = QtWidgets.QPushButton("Кнопка")
button.clicked.connect(on_clicked)
button.setAutoRepeat(True)
hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(button)
window.setLayout(hbox)
window.show()
sys.exit(app.exec())
