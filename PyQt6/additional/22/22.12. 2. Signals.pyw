from PyQt6 import QtWidgets
import sys

def on_clicked():
    progressBar.setValue(70)

def on_value_changed(n):
    print("on_value_changed", n)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QProgressBar")
window.resize(300, 100)
progressBar = QtWidgets.QProgressBar()
progressBar.setRange(0, 100)
progressBar.setValue(30)
progressBar.valueChanged[int].connect(on_value_changed)
button = QtWidgets.QPushButton("Изменить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(progressBar)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
