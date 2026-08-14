from PyQt6 import QtWidgets
import sys

def on_clicked():
    style = window.style()
    icon = style.standardIcon(
                         QtWidgets.QStyle.StandardPixmap.SP_DriveNetIcon)
    toolBox.setItemIcon(0, icon)
    button.setEnabled(False)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QToolBox")
window.resize(300, 250)
toolBox = QtWidgets.QToolBox()
button = QtWidgets.QPushButton("Установить иконку")
button.clicked.connect(on_clicked)
toolBox.addItem(QtWidgets.QLabel("Содержимое вкладки 1"), "Вкладка &1")
toolBox.addItem(QtWidgets.QLabel("Содержимое вкладки 2"), "Вкладка &2")
toolBox.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(toolBox)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
