from PyQt6 import QtWidgets
import sys

def on_clicked():
    print(dial.value())
    print(dial.sliderPosition())

app = QtWidgets.QApplication(sys.argv)
app.setStyle("fusion")
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QDial")
window.resize(300, 300)
dial = QtWidgets.QDial()
dial.setRange(0, 100)
dial.setValue(40)
dial.setNotchesVisible(True)
dial.setNotchTarget(2.0)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(dial)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
