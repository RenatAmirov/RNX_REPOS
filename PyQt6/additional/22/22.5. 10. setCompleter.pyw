from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLineEdit")
window.resize(300, 50)
lineEdit = QtWidgets.QLineEdit()
arr = ["кадр", "каменный", "камень", "камера"]
completer = QtWidgets.QCompleter(arr, window)
lineEdit.setCompleter(completer)
box = QtWidgets.QVBoxLayout()
box.addWidget(lineEdit)
window.setLayout(box)
window.show()
sys.exit(app.exec())
