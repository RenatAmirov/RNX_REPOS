from PyQt6 import QtWidgets
import sys

def on_clicked():
    toolBox.setUpdatesEnabled(False) # Для предотвращения мерцания
    index = toolBox.insertItem(0, QtWidgets.QLabel(
        "Содержимое вкладки 3"), "Вкладка &3")
    toolBox.setCurrentIndex(index)
    toolBox.setUpdatesEnabled(True) # Устанавливаем обратно
    button.setEnabled(False)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QToolBox")
window.resize(300, 250)
toolBox = QtWidgets.QToolBox()
button = QtWidgets.QPushButton("Добавить вкладку")
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
