from PyQt6 import QtWidgets
import sys

def on_clicked():
    progressBar.setValue(60)

def on_reset():
    progressBar.reset()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QProgressBar")
window.resize(300, 120)
progressBar = QtWidgets.QProgressBar()
progressBar.setRange(0, 100)
button = QtWidgets.QPushButton("Установить значение")
button.clicked.connect(on_clicked)
button2 = QtWidgets.QPushButton("Сбросить значение")
button2.clicked.connect(on_reset)
box = QtWidgets.QVBoxLayout()
box.addWidget(progressBar)
box.addWidget(button)
box.addWidget(button2)
window.setLayout(box)
window.show()
sys.exit(app.exec())
