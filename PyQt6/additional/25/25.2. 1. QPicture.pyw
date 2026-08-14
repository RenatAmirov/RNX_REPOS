from PyQt6 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 300)
        painter = QtGui.QPainter()
        pic = QtGui.QPicture()
        painter.begin(pic)
        painter.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.black))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.white))
        painter.drawRect(3, 3, 294, 294)
        painter.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.red, 1))
        painter.drawLine(10, 10, 290, 290)
        painter.end()
        pic.save("pic.dat")
    
    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        pic = QtGui.QPicture()
        pic.load("pic.dat")
        painter.drawPicture(0, 0, pic)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPainter")
    window.show()
    sys.exit(app.exec())
