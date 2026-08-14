from PyQt6 import QtWidgets
import sys

def on_clicked():
    print("Кнопка нажата")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QCommandLinkButton")
window.resize(300, 100)
button = QtWidgets.QCommandLinkButton("Текст на кнопке")
button.setDescription("Дополнительный текст")
button.clicked.connect(on_clicked)
hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(button)
window.setLayout(hbox)
window.show()
sys.exit(app.exec())
