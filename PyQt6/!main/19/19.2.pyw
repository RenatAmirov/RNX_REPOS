from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Вывод окна примерно по центру экрана")
window.resize(300, 100)
screen_size = window.screen().availableSize()
x = (screen_size.width() - window.width()) // 2
y = (screen_size.height() - window.height()) // 2
window.move(x, y)
window.show()
sys.exit(app.exec())
