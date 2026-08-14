from PyQt6 import QtWidgets
import sys

def on_toggled_radio1(status):
    print("radio1", status)

def on_toggled_radio2(status):
    print("radio2", status)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QRadioButton")
window.resize(300, 80)
radio1 = QtWidgets.QRadioButton("&Да")
radio2 = QtWidgets.QRadioButton("&Нет")
style = window.style()
icon1 = style.standardIcon(
              QtWidgets.QStyle.StandardPixmap.SP_DialogOkButton)
radio1.setIcon(icon1)
icon2 = style.standardIcon(
              QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical)
radio2.setIcon(icon2)
mainbox = QtWidgets.QVBoxLayout()
radio1.toggled["bool"].connect(on_toggled_radio1)
radio2.toggled["bool"].connect(on_toggled_radio2)
box = QtWidgets.QGroupBox("&Вы знаете язык Python?")
hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(radio1)
hbox.addWidget(radio2)
box.setLayout(hbox)
mainbox.addWidget(box)
window.setLayout(mainbox)
radio1.setChecked(True)
window.show()
sys.exit(app.exec())
