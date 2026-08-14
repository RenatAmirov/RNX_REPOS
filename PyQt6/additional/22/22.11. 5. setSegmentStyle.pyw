from PyQt6 import QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLCDNumber")
window.resize(500, 450)
label1 = QtWidgets.QLabel("Outline")
label1.setSizePolicy(QtWidgets.QSizePolicy(
    QtWidgets.QSizePolicy.Policy.Maximum, 
    QtWidgets.QSizePolicy.Policy.Maximum))
label2 = QtWidgets.QLabel("Filled")
label2.setSizePolicy(QtWidgets.QSizePolicy(
    QtWidgets.QSizePolicy.Policy.Maximum, 
    QtWidgets.QSizePolicy.Policy.Maximum))
label3 = QtWidgets.QLabel("Flat")
label3.setSizePolicy(QtWidgets.QSizePolicy(
    QtWidgets.QSizePolicy.Policy.Maximum, 
    QtWidgets.QSizePolicy.Policy.Maximum))
lcd = QtWidgets.QLCDNumber(9)
lcd.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Outline)
lcd.display(123456789)
lcd2 = QtWidgets.QLCDNumber(9)
lcd2.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
lcd2.display(123456789)
lcd3 = QtWidgets.QLCDNumber(9)
lcd3.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
lcd3.display(123456789)
box = QtWidgets.QVBoxLayout()
box.addWidget(label1)
box.addWidget(lcd)
box.addWidget(label2)
box.addWidget(lcd2)
box.addWidget(label3)
box.addWidget(lcd3)
window.setLayout(box)
window.show()
sys.exit(app.exec())
