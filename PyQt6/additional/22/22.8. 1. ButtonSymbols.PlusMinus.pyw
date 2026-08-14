from PyQt6 import QtWidgets
import sys

def on_clicked():
    print(spinBox.value())

app = QtWidgets.QApplication(sys.argv)
app.setStyle("windows")
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QSpinBox")
window.resize(300, 70)
spinBox = QtWidgets.QSpinBox()
spinBox.setMinimumHeight(35)
spinBox.setRange(0, 100)
spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.PlusMinus)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(spinBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
