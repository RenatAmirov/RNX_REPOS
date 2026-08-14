from PyQt6 import QtCore, QtWidgets, QtGui
import sys

def on_clicked():
    textEdit.setTextColor(QtGui.QColor("#FF0000"))

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setTextColor(QtCore.Qt.GlobalColor.blue)
textEdit.setPlainText("Значение по умолчанию")
button = QtWidgets.QPushButton("Изменить цвет текста")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
