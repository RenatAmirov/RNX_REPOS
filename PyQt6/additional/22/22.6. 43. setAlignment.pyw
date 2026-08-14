from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    textEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
textEdit.setPlainText("абзац 1\nабзац 2")
button = QtWidgets.QPushButton("Выравнивание по правому краю")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
