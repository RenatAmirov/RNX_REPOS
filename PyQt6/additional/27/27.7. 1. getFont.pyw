from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    (font, ok) = QtWidgets.QFontDialog.getFont(
        QtGui.QFont("Tahoma", 16), window, "Заголовок окна")
    if ok:
        print(font.family(), font.pointSize(), font.weight(),
              font.italic(), font.underline())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QFontDialog")
window.resize(300, 70)

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec())
