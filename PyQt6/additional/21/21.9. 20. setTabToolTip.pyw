from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget(
           flags=QtCore.Qt.WindowType.Dialog |
                 QtCore.Qt.WindowType.WindowContextHelpButtonHint |
                 QtCore.Qt.WindowType.WindowCloseButtonHint)
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 150)
tab = QtWidgets.QTabWidget()
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 1"), "Вкладка &1")
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 2"), "Вкладка &2")
tab.setTabToolTip(0, "Это текст подсказки для вкладки 1")
tab.setTabToolTip(1, "Это текст подсказки для вкладки 2")
tab.setTabWhatsThis(0, "Это текст справки для вкладки 1")
tab.setTabWhatsThis(1, "Это текст справки для вкладки 2")
tab.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(tab)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
