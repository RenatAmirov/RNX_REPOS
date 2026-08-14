from PyQt6 import QtWidgets
import sys

def on_clicked():
    tab.setCurrentIndex(1)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 150)
tab = QtWidgets.QTabWidget()
button = QtWidgets.QPushButton("Сделать вкладку 2 видимой")
button.clicked.connect(on_clicked)
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 1"), "Вкладка &1")
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 2"), "Вкладка &2")
tab.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(tab)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
