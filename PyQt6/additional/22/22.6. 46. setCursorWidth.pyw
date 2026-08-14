from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit("Значение по умолчанию")
textEdit.setCursorWidth(3)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
window.setLayout(box)
window.show()
sys.exit(app.exec())
