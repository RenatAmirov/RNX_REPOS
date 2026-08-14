from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    print(textBrowser.source().toString())
    textBrowser.home()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextBrowser")
window.resize(320, 240)
textBrowser = QtWidgets.QTextBrowser()
textBrowser.setSource(QtCore.QUrl("test.html"))
button = QtWidgets.QPushButton("Вывести адрес и перейти домой")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textBrowser)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
