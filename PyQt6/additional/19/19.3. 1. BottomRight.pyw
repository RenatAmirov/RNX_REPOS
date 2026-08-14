from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Вывод окна в нижнем правом углу экрана")
window.resize(300, 100)
window.move(window.width() * -2, 0)
window.show()
desktop = window.screen()
taskBarHeight = (desktop.geometry().height() - 
                 desktop.availableGeometry().height())
screen_size = desktop.availableSize()
x = screen_size.width() - window.frameSize().width()
y = screen_size.height() - window.frameSize().height() - taskBarHeight
window.move(x, y)
sys.exit(app.exec())
