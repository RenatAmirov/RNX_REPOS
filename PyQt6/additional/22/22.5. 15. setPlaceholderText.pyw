from PyQt6 import QtWidgets
import sys

def on_clicked():
    print(lineEdit.text(), lineEdit2.text())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLineEdit")
window.resize(300, 50)
lineEdit = QtWidgets.QLineEdit()
lineEdit.setPlaceholderText("Введите логин")
lineEdit2 = QtWidgets.QLineEdit()
lineEdit2.setPlaceholderText("Введите пароль")
lineEdit2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
button = QtWidgets.QPushButton("OK")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(lineEdit)
box.addWidget(lineEdit2)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
