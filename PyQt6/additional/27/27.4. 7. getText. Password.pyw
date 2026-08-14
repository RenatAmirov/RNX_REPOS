from PyQt6 import QtWidgets
import sys

def on_clicked():
    s, ok = QtWidgets.QInputDialog.getText(window, "Это заголовок окна",
                       "Введите пароль", 
                       echo=QtWidgets.QLineEdit.EchoMode.Password)
    if ok:
        print("Введено значение:", s)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QInputDialog")
window.resize(300, 70)

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec())
