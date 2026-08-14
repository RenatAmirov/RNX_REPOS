from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Вывод окна точно по центру экрана")
window.resize(300, 100)
window.move(window.width() * -2, 0)
window.show()
screen_size = window.screen().availableSize()
x = (screen_size.width() - window.frameSize().width()) // 2
y = (screen_size.height() - window.frameSize().height()) // 2
window.move(x, y)
sys.exit(app.exec())
