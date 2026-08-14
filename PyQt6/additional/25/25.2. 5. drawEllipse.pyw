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
        
        painter.setPen(QtGui.QPen(red, 2))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.green))
        painter.drawEllipse(50, 50, 80, 80)
        painter.drawEllipse(QtCore.QRect(150, 50, 80, 40))
        painter.drawEllipse(QtCore.QRectF(50., 150., 40., 80.))
        painter.drawEllipse(QtCore.QPoint(190, 190), 10, 30)
        painter.drawEllipse(QtCore.QPointF(190., 250.), 80., 20.)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPainter")
    window.show()
    sys.exit(app.exec())
