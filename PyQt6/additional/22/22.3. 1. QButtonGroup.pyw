from PyQt6 import QtWidgets
import sys

def on_clicked_group1(button):
    print("group1", button.text())

def on_clicked_group2(button):
    print("group2", button.text())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QButtonGroup")
window.resize(300, 80)
radio1 = QtWidgets.QRadioButton("Да")
radio2 = QtWidgets.QRadioButton("Нет")
radio3 = QtWidgets.QRadioButton("Да")
radio4 = QtWidgets.QRadioButton("Нет")
buttonGroup1 = QtWidgets.QButtonGroup(window)
buttonGroup1.addButton(radio1, 1)
buttonGroup1.addButton(radio2, 2)
buttonGroup1.buttonClicked.connect(on_clicked_group1)
buttonGroup2 = QtWidgets.QButtonGroup(window)
buttonGroup2.addButton(radio3, 1)
buttonGroup2.addButton(radio4, 2)
buttonGroup2.buttonClicked.connect(on_clicked_group2)
label1 = QtWidgets.QLabel("Вы знаете язык Python?")
label2 = QtWidgets.QLabel("Вы знаете библиотеку PyQt?")
box = QtWidgets.QVBoxLayout()
box.addWidget(label1)
box.addWidget(radio1)
box.addWidget(radio2)
box.addWidget(label2)
box.addWidget(radio3)
box.addWidget(radio4)
window.setLayout(box)
radio1.setChecked(True)
radio3.setChecked(True)
window.show()
sys.exit(app.exec())
