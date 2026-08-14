from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QGroupBox")
window.resize(250, 80)
mainbox = QtWidgets.QVBoxLayout()  # Создаем главный контейнер
radio1 = QtWidgets.QRadioButton("&Да")
radio2 = QtWidgets.QRadioButton("&Нет")
box = QtWidgets.QGroupBox("&Вы знаете язык Python?") # Объект группы
hbox = QtWidgets.QHBoxLayout()     # Создаем второй контейнер — для группы
hbox.addWidget(radio1)             # Добавляем компоненты во второй контейнер
hbox.addWidget(radio2)
box.setLayout(hbox)                # Добавляем второй контейнер в группу
mainbox.addWidget(box)             # Добавляем группу в главный контейнер
window.setLayout(mainbox)          # Помещаем главный контейнер в окно
radio1.setChecked(True)            # Выбираем первый переключатель
window.show()
sys.exit(app.exec())
