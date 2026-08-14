from PyQt6 import QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 300)
        self.img = QtGui.QImage()
        f = open("photo.jpg", "rb")
        img = f.read()
        f.close()
        self.pix = QtGui.QPixmap()
        self.pix.loadFromData(img, "JPG")
    
    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPixmap")
    window.show()
    sys.exit(app.exec())
