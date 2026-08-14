from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    print(slider.value())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QSlider")
window.resize(300, 100)
slider = QtWidgets.QSlider()
slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider.setMinimum(0)
slider.setMaximum(100)
slider.setValue(40)
slider.setInvertedAppearance(True)
slider.setInvertedControls(False)
slider.setSingleStep(10)
slider.setPageStep(20)
slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(slider)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
