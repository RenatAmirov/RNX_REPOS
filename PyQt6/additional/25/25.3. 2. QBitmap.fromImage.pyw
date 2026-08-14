from PyQt6 import QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(600, 600)
        img = QtGui.QImage("photo.jpg", "JPG")
        self.pix = QtGui.QBitmap.fromImage(img)
        m = QtGui.QTransform()
        m.rotate(90.0)
        self.pix = self.pix.transformed(m)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QBitmap")
    window.show()
    sys.exit(app.exec())
