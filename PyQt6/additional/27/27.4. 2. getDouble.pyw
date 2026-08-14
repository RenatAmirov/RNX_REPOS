from PyQt6 import QtWidgets
import sys

def on_clicked():
    n, ok = QtWidgets.QInputDialog.getDouble(window,
                       "Это заголовок окна", "Это текст подсказки", 
                       value=50.0, min=0.0, max=100.0, decimals=2)
    if ok:
        print("Введено значение:", n)

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
