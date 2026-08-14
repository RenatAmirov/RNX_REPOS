from PyQt6 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 300)
    
    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        black = QtCore.Qt.GlobalColor.black
        white = QtCore.Qt.GlobalColor.white
        red = QtCore.Qt.GlobalColor.red
        painter.setPen(QtGui.QPen(black))
        painter.setBrush(QtGui.QBrush(white))
        painter.drawRect(3, 3, 294, 294)
        painter.drawLine(20, 20, 20, 280)
        painter.drawLine(280, 20, 280, 280)
        painter.setPen(QtGui.QPen(red, 15,
                                  cap=QtCore.Qt.PenCapStyle.FlatCap))
        painter.drawLine(20, 50, 280, 50)
        painter.setPen(QtGui.QPen(red, 15,
                                  cap=QtCore.Qt.PenCapStyle.SquareCap))
        painter.drawLine(20, 100, 280, 100)
        painter.setPen(QtGui.QPen(red, 15,
                                  cap=QtCore.Qt.PenCapStyle.RoundCap))
        painter.drawLine(20, 150, 280, 150)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPen")
    window.show()
    sys.exit(app.exec())
