from PyQt6 import QtWidgets
import sys

def on_clicked():
    print(spinBox.text())
    print(spinBox.prefix())
    print(spinBox.suffix())
    print(spinBox.value(), type(spinBox.value()))
    print(spinBox.cleanText(), type(spinBox.cleanText()))

def on_value_changed(x):
    print("on_value_changed", x)

def on_text_changed(s):
    print("on_text_changed", s)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QDoubleSpinBox")
window.resize(300, 70)
spinBox = QtWidgets.QDoubleSpinBox()
spinBox.setRange(0.0, 100.0)
spinBox.setValue(10.0)
spinBox.setSingleStep(5.0)
spinBox.setDecimals(2)
spinBox.setPrefix("текст до (")
spinBox.setSuffix(") текст после")
spinBox.valueChanged.connect(on_value_changed)
spinBox.textChanged.connect(on_text_changed)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(spinBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
