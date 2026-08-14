from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()              # Родительский компонент — окно
window.setWindowTitle("QHBoxLayout")
window.resize(300, 60)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
button3 = QtWidgets.QPushButton("3")
button4 = QtWidgets.QPushButton("4")
hbox = QtWidgets.QHBoxLayout()            # Создаем контейнер
hbox.addWidget(button1)                   # Добавляем компоненты
hbox.addWidget(button2)
hbox.addWidget(button3)
hbox.addWidget(button4)
window.setLayout(hbox)                    # Привязываем контейнер к родителю
window.show()
sys.exit(app.exec())
