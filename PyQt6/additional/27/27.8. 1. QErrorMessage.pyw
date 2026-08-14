from PyQt6 import QtWidgets
import sys

def on_clicked():
    dialog.showMessage("Это текст сообщения об ошибке")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QErrorMessage")
window.resize(300, 70)

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)

dialog = QtWidgets.QErrorMessage(window)

window.setWindowTitle("Класс QErrorMessage")
window.show()

sys.exit(app.exec())
