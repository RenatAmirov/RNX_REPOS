from PyQt6 import QtWidgets
import sys

def on_menu_item1():
    print("Выбран пункт 1")

def on_menu_item2():
    print("Выбран пункт 2")

def on_menu_item3():
    print("Выбран пункт 3")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
button = QtWidgets.QPushButton("Кнопка с меню")
menu = QtWidgets.QMenu()
menu.addAction("Пункт 1", on_menu_item1)
menu.addAction("Пункт 2", on_menu_item2)
menu.addAction("Пункт 3", on_menu_item3)
button.setMenu(menu)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
