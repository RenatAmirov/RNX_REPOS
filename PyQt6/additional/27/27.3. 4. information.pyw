from PyQt6 import QtWidgets
import sys

def on_clicked():
    QtWidgets.QMessageBox.information(window, "Текст заголовка", 
               "Текст сообщения",
               buttons=QtWidgets.QMessageBox.StandardButton.Close,
               defaultButton=QtWidgets.QMessageBox.StandardButton.Close)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QMessageBox")
window.resize(300, 70)

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec())
