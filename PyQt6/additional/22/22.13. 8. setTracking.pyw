from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    print(slider.value())
    print(slider.sliderPosition())

def on_value_changed(pos):
    print("on_value_changed")
    print("pos - ", pos)
    print("value - ", slider.value())
    print("sliderPosition - ", slider.sliderPosition())

def on_slider_moved(pos):
    print("on_slider_moved")
    print("pos - ", pos)
    print("value - ", slider.value())
    print("sliderPosition - ", slider.sliderPosition())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QSlider")
window.resize(300, 100)
slider = QtWidgets.QSlider()
slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider.setMinimum(0)
slider.setMaximum(100)
slider.setSliderPosition(40)
slider.setSingleStep(10)
slider.setPageStep(20)
slider.setTracking(False)
slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
slider.valueChanged[int].connect(on_value_changed)
slider.sliderMoved[int].connect(on_slider_moved)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(slider)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
