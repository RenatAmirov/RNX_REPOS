from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 150)
tab = QtWidgets.QTabWidget()
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 1"),
           "Вкладка с длинным названием")
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 2"),
           "Вкладка &2")
tab.setElideMode(QtCore.Qt.TextElideMode.ElideRight)
tab.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(tab)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
