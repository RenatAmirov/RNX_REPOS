from PyQt6 import QtWidgets
import sys

def insert_tab():
    tab.setUpdatesEnabled(False) # Для предотвращения мерцания
    ind = tab.insertTab(0, QtWidgets.QLabel("Содержимое вкладки 3"), 
                        "Вкладка &3")
    tab.setCurrentIndex(ind)
    tab.setUpdatesEnabled(True) # Устанавливаем обратно
    button.setEnabled(False)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 150)
tab = QtWidgets.QTabWidget()
button = QtWidgets.QPushButton("Добавить вкладку")
button.clicked.connect(insert_tab)
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 1"), "Вкладка &1")
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 2"), "Вкладка &2")
tab.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(tab)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
