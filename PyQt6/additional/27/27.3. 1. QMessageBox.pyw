from PyQt6 import QtWidgets
import sys

def on_clicked():
    dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical, 
                       "Текст заголовка", "Текст сообщения",
                       buttons=QtWidgets.QMessageBox.StandardButton.Ok | 
                               QtWidgets.QMessageBox.StandardButton.Cancel,
                       parent=window)
    result = dialog.exec()
    if result == QtWidgets.QMessageBox.StandardButton.Ok:
        print("Нажата кнопка OK")
    elif result == QtWidgets.QMessageBox.StandardButton.Cancel:
        print("Нажата кнопка Cancel, кнопка Закрыть или клавиша <Esc>")
    else:
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
