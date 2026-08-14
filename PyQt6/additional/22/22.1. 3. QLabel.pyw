from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
label = QtWidgets.QLabel("Текст надписи", flags=QtCore.Qt.WindowType.Window)
label.setWindowTitle("Класс QLabel")
label.resize(300, 50)
label.show()
sys.exit(app.exec())
