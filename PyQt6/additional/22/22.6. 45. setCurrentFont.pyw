from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    textEdit.setCurrentFont(QtGui.QFont("Tahoma", pointSize=12, 
                            weight=QtGui.QFont.Weight.Normal, italic=True))

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setCurrentFont(QtGui.QFont("Tahoma", 30, QtGui.QFont.Weight.Bold))
textEdit.setPlainText("Значение по умолчанию")
button = QtWidgets.QPushButton("Изменить шрифт")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
