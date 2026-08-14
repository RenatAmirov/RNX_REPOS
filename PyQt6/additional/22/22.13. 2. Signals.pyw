from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    slider.setMinimum(10)
    slider.setMaximum(90)

def on_value_changed(pos):
    print("on_value_changed", pos)

def on_slider_moved(pos):
    print("on_slider_moved", pos)

def on_slider_pressed():
    print("on_slider_pressed")

def on_slider_released():
    print("on_slider_released")

def on_range_changed(min, max):
    print("on_range_changed", min, max)

def on_action_triggered(a):
    print("on_action_triggered", a)

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
slider.sliderPressed.connect(on_slider_pressed)
slider.sliderReleased.connect(on_slider_released)
slider.rangeChanged[int, int].connect(on_range_changed)
slider.actionTriggered[int].connect(on_action_triggered)
button = QtWidgets.QPushButton("Изменить диапазон значений")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(slider)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
