from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 120)
tab = QtWidgets.QTabWidget()
style = window.style()
icon1 = style.standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DriveHDIcon)
icon2 = style.standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DriveCDIcon)
icon3 = style.standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DriveNetIcon)
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 1"), icon1,
           "Вкладка &1")
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 2"), icon2,
           "Вкладка &2")
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 3"), icon3,
           "Вкладка &3")
tab.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(tab)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
