from PyQt6 import QtWidgets
import sys

def on_clicked():
    s, ok = QtWidgets.QInputDialog.getItem(window, "Это заголовок окна",
              "Это текст подсказки", ["Пункт 1", "Пункт 2", "Пункт 3"],
              current=1, editable=False)
    if ok:
        print("Текст выбранного пункта:", s)

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
