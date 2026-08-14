from PyQt6 import QtWidgets
import sys

def on_clicked():
    print(spinBox.text())

def on_editing_finished():
    print("on_editing_finished")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QSpinBox")
window.resize(300, 70)
spinBox = QtWidgets.QSpinBox()
spinBox.setRange(0, 100)
spinBox.editingFinished.connect(on_editing_finished)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(spinBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
