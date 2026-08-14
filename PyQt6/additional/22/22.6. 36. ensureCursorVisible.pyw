from PyQt6 import QtWidgets
import sys

def on_clicked():
    textEdit.setFocus()
    textEdit.ensureCursorVisible()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
textEdit.setPlainText("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                      "\n\n\n\n\n\n\n\n\n\nЗначение по умолчанию")
button = QtWidgets.QPushButton("Показать позицию с курсором")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
