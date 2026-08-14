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
        painter.setPen(QtGui.QPen(red, 5))
        line1 = QtCore.QLine(QtCore.QPoint(20, 50),
                             QtCore.QPoint(280, 50))
        painter.drawLine(line1)
        line2 = QtCore.QLine(20, 100, 280, 100)
        painter.drawLine(line2)
        print(line1.p1(), line1.p2())
        print(line2.x1(), line2.y1(), line2.x2(), line2.y2())
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QLine")
    window.show()
    sys.exit(app.exec())
