from PyQt6 import QtWidgets
import sys

def on_clicked():
    textEdit.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit(
"""setLineWrapMode() задает режим переноса строк. В качестве значения могут быть указаны элементы перечисления LineWrapMode из класса QTextEdit.""")
textEdit.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
textEdit.setLineWrapColumnOrWidth(70)
button = QtWidgets.QPushButton("Переключить режим")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
