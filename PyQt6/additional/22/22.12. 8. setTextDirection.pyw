from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    progressBar.setValue(70)
    progressBar2.setValue(70)

def on_reset():
    progressBar.reset()
    progressBar2.reset()

app = QtWidgets.QApplication(sys.argv)
app.setStyle("motif")
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QProgressBar")
window.resize(500, 400)
progressBar = QtWidgets.QProgressBar()
progressBar.setRange(0, 100)
progressBar.setOrientation(QtCore.Qt.Orientation.Vertical)
progressBar.setTextDirection(
               QtWidgets.QProgressBar.Direction.TopToBottom)
progressBar2 = QtWidgets.QProgressBar()
progressBar2.setRange(0, 100)
progressBar2.setOrientation(QtCore.Qt.Orientation.Vertical)
progressBar2.setTextDirection(
                QtWidgets.QProgressBar.Direction.BottomToTop)
button = QtWidgets.QPushButton("Установить значение")
button.clicked.connect(on_clicked)
button2 = QtWidgets.QPushButton("Сбросить значение")
button2.clicked.connect(on_reset)
box = QtWidgets.QHBoxLayout()
box.addWidget(progressBar)
box.addWidget(progressBar2)
box.addWidget(button)
box.addWidget(button2)
window.setLayout(box)
window.show()
sys.exit(app.exec())
