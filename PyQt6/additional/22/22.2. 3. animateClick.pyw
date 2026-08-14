from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked_button1():
    print("Кнопка нажата")
    
def on_clicked_button2():
    button1.animateClick()
    
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
button1 = QtWidgets.QPushButton("Кнопка")
button2 = QtWidgets.QPushButton("Нажми меня")
button1.clicked.connect(on_clicked_button1)
button2.clicked.connect(on_clicked_button2)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
