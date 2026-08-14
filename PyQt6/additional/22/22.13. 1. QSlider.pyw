from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    print(slider.value())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QSlider")
window.resize(300, 100)
slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
slider.setRange(0, 100)
slider.setValue(50)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(slider)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
