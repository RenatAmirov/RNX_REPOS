from PyQt6 import QtWidgets
import sys

def on_clicked():
    dial.setRange(10, 90)

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
window.setWindowTitle("Класс QDial")
window.resize(300, 300)
dial = QtWidgets.QDial()
dial.setRange(0, 100)
dial.setValue(40)
dial.setNotchesVisible(True)
dial.setNotchTarget(2.0)
dial.valueChanged[int].connect(on_value_changed)
dial.sliderMoved[int].connect(on_slider_moved)
dial.sliderPressed.connect(on_slider_pressed)
dial.sliderReleased.connect(on_slider_released)
dial.rangeChanged[int, int].connect(on_range_changed)
dial.actionTriggered[int].connect(on_action_triggered)
button = QtWidgets.QPushButton("Изменить диапазон значений")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(dial)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
