from PyQt6 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 150)
        self.my_icon = QtGui.QIcon()
        self.my_icon.addFile("icon1.png", QtCore.QSize(32, 32), 
                             mode=QtGui.QIcon.Mode.Normal)
        self.my_icon.addPixmap(QtGui.QPixmap("icon2.png"), 
                               mode=QtGui.QIcon.Mode.Normal)
        self.my_icon.addFile("icon3.png", QtCore.QSize(32, 32),
                             mode=QtGui.QIcon.Mode.Disabled)
        self.pix1 = self.my_icon.pixmap(32, 32, mode=QtGui.QIcon.Mode.Normal)
        self.pix2 = self.my_icon.pixmap(16, 16, mode=QtGui.QIcon.Mode.Normal)
        self.pix3 = self.my_icon.pixmap(32, 32, 
                                        mode=QtGui.QIcon.Mode.Disabled)
        self.my_icon2 = self.style().standardIcon(
                        QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical)
        self.pix4 = self.my_icon2.pixmap(32, 32, mode=QtGui.QIcon.Mode.Normal)
        self.pix5 = self.my_icon2.pixmap(32, 32, 
                                         mode=QtGui.QIcon.Mode.Disabled)
        print(self.my_icon.availableSizes(mode=QtGui.QIcon.Mode.Normal))
        print(self.my_icon.availableSizes(mode=QtGui.QIcon.Mode.Disabled))
        print(self.my_icon.actualSize(QtCore.QSize(16, 16),
                                      mode=QtGui.QIcon.Mode.Normal))

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(5, 10, self.pix1)
        painter.drawPixmap(50, 10, self.pix2)
        painter.drawPixmap(100, 10, self.pix3)
        painter.drawPixmap(150, 10, self.pix4)
        painter.drawPixmap(200, 10, self.pix5)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QIcon")
    window.show()
    sys.exit(app.exec())
