from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    textEdit.setWordWrapMode(QtGui.QTextOption.WrapMode.WordWrap)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit(
"""setWordWrapMode() задает режим переноса строк. В качестве значения могут быть указаны элементы перечисления WrapMode из класса QTextOption.""")
textEdit.setWordWrapMode(QtGui.QTextOption.WrapMode.NoWrap)
button = QtWidgets.QPushButton("Переключить режим")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
