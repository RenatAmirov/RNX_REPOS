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
        painter.drawPoints(QtCore.QPoint(50, 50),
                           QtCore.QPoint(150, 50),
                           QtCore.QPoint(250, 50))
        painter.drawPoints(QtCore.QPointF(50., 100.),
                           QtCore.QPointF(150., 100.),
                           QtCore.QPointF(250., 100.))
        painter.setPen(QtGui.QPen(black, 5))
        polygon = QtGui.QPolygon([
                           QtCore.QPoint(20, 150),
                           QtCore.QPoint(280, 150),
                           QtCore.QPoint(150, 250)])
        painter.drawPoints(polygon)
        painter.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.green, 5))
        polygonF = QtGui.QPolygonF([
                           QtCore.QPointF(20., 250.),
                           QtCore.QPointF(280., 250.),
                           QtCore.QPointF(150., 150.)])
        painter.drawPoints(polygonF)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPainter")
    window.show()
    sys.exit(app.exec())
