from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    print(scrollBar.value())
    print(scrollBar.sliderPosition())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QScrollBar")
window.resize(300, 100)
scrollBar = QtWidgets.QScrollBar(QtCore.Qt.Orientation.Horizontal)
scrollBar.setRange(0, 100)
scrollBar.setValue(40)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(scrollBar)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
