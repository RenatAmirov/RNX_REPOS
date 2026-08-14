from PyQt6 import QtCore, QtWidgets, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowFlags(QtCore.Qt.WindowType.Window |
                      QtCore.Qt.WindowType.FramelessWindowHint)
window.setWindowTitle("Создание окна произвольной формы")
window.resize(300, 300)
pixmap = QtGui.QPixmap("background.png")
pal = window.palette()
pal.setBrush(QtGui.QPalette.ColorGroup.Normal, QtGui.QPalette.ColorRole.Window,
             QtGui.QBrush(pixmap))
pal.setBrush(QtGui.QPalette.ColorGroup.Inactive,
             QtGui.QPalette.ColorRole.Window, QtGui.QBrush(pixmap))
window.setPalette(pal)
window.setMask(pixmap.mask())
button = QtWidgets.QPushButton("Закрыть окно", window)
button.setFixedSize(150, 30)
button.move(75, 135)
button.clicked.connect(app.quit)
window.show()
sys.exit(app.exec())
