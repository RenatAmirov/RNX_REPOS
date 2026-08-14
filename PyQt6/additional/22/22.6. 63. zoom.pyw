from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit("Значение <b>по умолчанию</b>")
button = QtWidgets.QPushButton("Уменьшить")
button.clicked.connect(textEdit.zoomOut)
button2 = QtWidgets.QPushButton("Увеличить")
button2.clicked.connect(textEdit.zoomIn)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
box.addWidget(button2)
window.setLayout(box)
window.show()
sys.exit(app.exec())
