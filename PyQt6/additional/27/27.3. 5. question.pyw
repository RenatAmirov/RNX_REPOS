from PyQt6 import QtWidgets
import sys

def on_clicked():
    result = QtWidgets.QMessageBox.question(window, "Текст заголовка", 
               "Вы действительно хотите выполнить действие?",
               buttons=QtWidgets.QMessageBox.StandardButton.Yes |
                       QtWidgets.QMessageBox.StandardButton.No |
                       QtWidgets.QMessageBox.StandardButton.Cancel,
               defaultButton=QtWidgets.QMessageBox.StandardButton.Cancel)
    match result:
        case QtWidgets.QMessageBox.StandardButton.Yes:
            print("Нажата кнопка Yes")
        case QtWidgets.QMessageBox.StandardButton.No:
            print("Нажата кнопка No")
        case QtWidgets.QMessageBox.StandardButton.Cancel:
            print("Нажата кнопка Cancel, кнопка Закрыть или клавиша <Esc>")
        case _:
            print("Нажата кнопка", result)

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
