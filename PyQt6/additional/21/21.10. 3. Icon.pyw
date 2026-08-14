from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QToolBox")
window.resize(300, 150)
toolBox = QtWidgets.QToolBox()
style = window.style()
icon1 = style.standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DriveHDIcon)
icon2 = style.standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DriveCDIcon)
icon3 = style.standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DriveNetIcon)
toolBox.addItem(QtWidgets.QLabel("Содержимое вкладки 1"),
                icon1, "Вкладка &1")
toolBox.addItem(QtWidgets.QLabel("Содержимое вкладки 2"),
                icon2, "Вкладка &2")
toolBox.addItem(QtWidgets.QLabel("Содержимое вкладки 3"),
                icon3, "Вкладка &3")
toolBox.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(toolBox)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
