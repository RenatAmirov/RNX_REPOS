from PyQt6 import QtWidgets
import sys

def on_clicked():
    print(progressBar.value())
    print(progressBar.text())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QProgressBar")
window.resize(300, 100)
progressBar = QtWidgets.QProgressBar()
progressBar.setRange(0, 100)
progressBar.setValue(70)
progressBar.setInvertedAppearance(True)
button = QtWidgets.QPushButton("Вывести текст и значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(progressBar)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
