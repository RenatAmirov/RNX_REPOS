from PyQt6 import QtWidgets
import sys

def remove_tab():
    tab.removeTab(0)
    button.setEnabled(False)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 150)
tab = QtWidgets.QTabWidget()
button = QtWidgets.QPushButton("Удалить вкладку")
button.clicked.connect(remove_tab)
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 1"), "Вкладка &1")
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 2"), "Вкладка &2")
tab.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(tab)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
