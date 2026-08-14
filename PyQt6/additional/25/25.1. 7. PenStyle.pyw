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
        painter.setPen(QtGui.QPen(red, 4,
                                  style=QtCore.Qt.PenStyle.SolidLine))
        painter.drawLine(20, 50, 280, 50)
        painter.setPen(QtGui.QPen(red, 4,
                                  style=QtCore.Qt.PenStyle.DashLine))
        painter.drawLine(20, 100, 280, 100)
        painter.setPen(QtGui.QPen(red, 4,
                                  style=QtCore.Qt.PenStyle.DotLine))
        painter.drawLine(20, 150, 280, 150)
        painter.setPen(QtGui.QPen(red, 4,
                                  style=QtCore.Qt.PenStyle.DashDotLine))
        painter.drawLine(20, 200, 280, 200)
        painter.setPen(QtGui.QPen(red, 4,
                                  style=QtCore.Qt.PenStyle.DashDotDotLine))
        painter.drawLine(20, 250, 280, 250)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPen")
    window.show()
    sys.exit(app.exec())
