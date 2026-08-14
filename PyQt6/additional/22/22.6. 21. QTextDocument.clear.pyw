from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    textEdit.document().clear()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
document = QtGui.QTextDocument()
document.setPlainText("Текст внутри поля")
textEdit.setDocument(document)
button = QtWidgets.QPushButton("Очистить")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
