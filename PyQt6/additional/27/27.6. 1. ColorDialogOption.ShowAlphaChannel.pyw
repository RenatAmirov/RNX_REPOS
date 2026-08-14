from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    color = QtWidgets.QColorDialog.getColor(QtGui.QColor("#ff0000"), 
            window, "Заголовок окна",
            QtWidgets.QColorDialog.ColorDialogOption.ShowAlphaChannel)
    print(type(color))
    if color.isValid():
        print(color.red(), color.green(), color.blue(), color.alpha())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QColorDialog")
window.resize(300, 70)

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec())
