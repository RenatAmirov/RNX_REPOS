from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    if lineEdit.hasAcceptableInput():
        print(lineEdit.text())
    else:
        print("Значение не соответствует условию")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLineEdit")
window.resize(300, 50)
lineEdit = QtWidgets.QLineEdit()
lineEdit.setValidator(
         QtGui.QDoubleValidator(0.0, 100.0, 2, window))
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(lineEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
