from PyQt6 import QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(400, 400)
        self.img = QtGui.QImage(300, 300, 
                         QtGui.QImage.Format.Format_ARGB32_Premultiplied)
        self.img.fill(QtGui.QColor("#ff0000").rgb())
        color = QtGui.QColor(self.img.pixel(1, 1))
        print(color.name(), color.getRgb())

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.img)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QImage")
    window.show()
    sys.exit(app.exec())
