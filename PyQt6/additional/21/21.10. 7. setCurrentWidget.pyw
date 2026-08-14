from PyQt6 import QtWidgets
import sys

def on_clicked():
    toolBox.setCurrentWidget(label2)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QToolBox")
window.resize(300, 250)
toolBox = QtWidgets.QToolBox()
button = QtWidgets.QPushButton("Сделать вкладку 2 видимой")
button.clicked.connect(on_clicked)
label1 = QtWidgets.QLabel("Содержимое вкладки 1")
label2 = QtWidgets.QLabel("Содержимое вкладки 2")
toolBox.addItem(label1, "Вкладка &1")
toolBox.addItem(label2, "Вкладка &2")
toolBox.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(toolBox)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
