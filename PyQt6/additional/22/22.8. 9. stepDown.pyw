from PyQt6 import QtWidgets
import sys

def on_clicked():
    spinBox.stepDown()

def on_clicked2():
    spinBox.stepUp()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QSpinBox")
window.resize(300, 70)
spinBox = QtWidgets.QSpinBox()
spinBox.setRange(0, 100)
button = QtWidgets.QPushButton("-")
button.clicked.connect(on_clicked)
button2 = QtWidgets.QPushButton("+")
button2.clicked.connect(on_clicked2)
box = QtWidgets.QVBoxLayout()
box.addWidget(spinBox)
box.addWidget(button)
box.addWidget(button2)
window.setLayout(box)
window.show()
sys.exit(app.exec())
