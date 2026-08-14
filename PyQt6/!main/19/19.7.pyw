from PyQt6 import QtGui, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Смена значка в заголовке окна")
window.resize(300, 100)
ico = QtGui.QIcon("icon.png")
window.setWindowIcon(ico)             # Значок для окна
app.setWindowIcon(ico)                # Значок программы
window.show()
sys.exit(app.exec())
