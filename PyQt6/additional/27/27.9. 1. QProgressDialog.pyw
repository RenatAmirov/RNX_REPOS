from PyQt6 import QtWidgets
import sys, time

def on_clicked():
    dialog = QtWidgets.QProgressDialog("Выполняется операция", "&Отмена", 
                                       0, 20, window)
    dialog.setWindowTitle("Выполнение операции")
    dialog.setModal(True)
    dialog.setValue(0)
    dialog.show()
    dialog.resize(300, 100)
    for i in range(1, 21):
        dialog.setValue(i)
        if dialog.wasCanceled():
            break
        time.sleep(1)               # "Засыпаем" на 1 секунду
        QtWidgets.QApplication.instance().processEvents()
        # Запускаем оборот цикла (если нужно)
        print("step -", i)
    dialog.close()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QProgressDialog")
window.resize(300, 70)

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec())
