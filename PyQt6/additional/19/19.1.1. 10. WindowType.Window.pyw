from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowFlags(QtCore.Qt.WindowType.Window)
window.setWindowTitle("Заголовок окна")
window.resize(300, 50)
btn = QtWidgets.QPushButton("Закрыть окно", window)
btn.setGeometry(50, 10, 200, 30)
btn.clicked.connect(app.quit)
screen_size = window.screen().availableSize()
x = (screen_size.width() - window.width()) // 2
y = (screen_size.height() - window.height()) // 2
window.move(x, y)
window.show()
sys.exit(app.exec())
