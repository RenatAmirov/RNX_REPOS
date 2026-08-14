from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Вывод окна по центру экрана")
window.resize(300, 100)
desktop = window.screen()
window.move(desktop.geometry().center() - window.rect().center())
window.show()
sys.exit(app.exec())
