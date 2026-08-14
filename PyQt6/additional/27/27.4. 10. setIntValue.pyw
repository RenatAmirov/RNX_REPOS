from PyQt6 import QtWidgets
import sys

def on_value_changed(n):
    print("on_value_changed", n)

def on_value_selected(n):
    print("on_value_selected", n)

def on_clicked():
    dialog = QtWidgets.QInputDialog(window)
    dialog.setWindowTitle("Это заголовок окна")
    dialog.setLabelText("Это текст подсказки")
    dialog.setOkButtonText("&Ввод")
    dialog.setCancelButtonText("&Отмена")
    dialog.setInputMode(QtWidgets.QInputDialog.InputMode.IntInput)
    dialog.setIntRange(0, 100)
    dialog.setIntStep(10)
    dialog.setIntValue(50)
    dialog.intValueChanged[int].connect(on_value_changed)
    dialog.intValueSelected[int].connect(on_value_selected)
    result = dialog.exec()
    if result == QtWidgets.QDialog.DialogCode.Accepted:
        print(dialog.intValue())
    else:
        print("Нажата кнопка Cancel")

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
