from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    textEdit.setFontWeight(QtGui.QFont.Weight.Normal)
    print(textEdit.fontWeight())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setFontWeight(QtGui.QFont.Weight.Bold)
textEdit.setPlainText("Значение по умолчанию")
button = QtWidgets.QPushButton("Изменить жирность шрифта")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
