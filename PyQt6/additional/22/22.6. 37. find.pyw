from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    textEdit.setFocus()
    textEdit.find("текст", 
                  QtGui.QTextDocument.FindFlag.FindCaseSensitively |
                  QtGui.QTextDocument.FindFlag.FindBackward)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setPlainText("текст\nтекст\nТЕКСТ\nтекст\nтекст\nтекст\nтекст"
                      "\nтекст\nтекст\nтекст\n")
button = QtWidgets.QPushButton(
    "Найти в обратном порядке с учетом регистра")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
