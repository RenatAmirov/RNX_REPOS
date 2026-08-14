from PyQt6 import QtWidgets
import sys

def on_clicked():
    print(lineEdit.text())
    lineEdit.setSelection(0, 6)
    print(lineEdit.selectedText())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLineEdit")
window.resize(300, 50)
lineEdit = QtWidgets.QLineEdit()
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(lineEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
