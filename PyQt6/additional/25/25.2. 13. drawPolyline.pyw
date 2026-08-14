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
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setPen(QtGui.QPen(black))
        painter.setBrush(QtGui.QBrush(white))
        painter.drawRect(3, 3, 294, 294)
        
        painter.setPen(QtGui.QPen(red, 2,
                                  style=QtCore.Qt.PenStyle.SolidLine))
        painter.drawPolyline(QtCore.QPoint(20, 30),
                QtCore.QPoint(280, 30), QtCore.QPoint(20, 80),
                QtCore.QPoint(280, 80))
        painter.drawPolyline(QtCore.QPointF(20., 100.),
                QtCore.QPointF(280., 100.), QtCore.QPointF(20., 140.),
                QtCore.QPointF(280., 140.))
        painter.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.blue, 5))
        polygon = QtGui.QPolygon([
                           QtCore.QPoint(20, 150),
                           QtCore.QPoint(280, 150),
                           QtCore.QPoint(150, 250)])
        painter.drawPolyline(polygon)
        painter.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.green, 5))
        polygonF = QtGui.QPolygonF([
                           QtCore.QPointF(20., 250.),
                           QtCore.QPointF(280., 250.),
                           QtCore.QPointF(150., 150.)])
        painter.drawPolyline(polygonF)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPainter")
    window.show()
    sys.exit(app.exec())
