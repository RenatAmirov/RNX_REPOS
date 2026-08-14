from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    textBrowser.backward()

def on_clicked2():
    textBrowser.forward()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextBrowser")
window.resize(320, 240)
textBrowser = QtWidgets.QTextBrowser()
textBrowser.setSource(QtCore.QUrl("test.html"))
button = QtWidgets.QPushButton("Назад")
button.clicked.connect(on_clicked)
button2 = QtWidgets.QPushButton("Вперед")
button2.clicked.connect(on_clicked2)
box = QtWidgets.QVBoxLayout()
box.addWidget(textBrowser)
box.addWidget(button)
box.addWidget(button2)
window.setLayout(box)
window.show()
sys.exit(app.exec())
