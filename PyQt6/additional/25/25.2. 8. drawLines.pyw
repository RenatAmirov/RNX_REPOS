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
        painter.drawLines(QtCore.QLine(20, 50, 280, 50), 
                QtCore.QLine(20, 60, 280, 60))
        painter.drawLines(QtCore.QLineF(20., 70., 280., 70.),
                QtCore.QLineF(20., 80., 280., 80.))
        painter.drawLines(QtCore.QLine(20, 90, 280, 90), 
                QtCore.QLine(20, 100, 280, 100))
        painter.drawLines([QtCore.QLineF(20., 110., 280., 110.),
                QtCore.QLineF(20., 120., 280., 120.)])
        painter.drawLines(QtCore.QPoint(20, 130),
                QtCore.QPoint(280, 130), QtCore.QPoint(20, 140),
                QtCore.QPoint(280, 140))
        painter.drawLines(QtCore.QPointF(20., 150.),
                QtCore.QPointF(280., 150.), QtCore.QPointF(20., 160.),
                QtCore.QPointF(280., 160.))
        painter.drawLines(QtCore.QPoint(20, 170),
                QtCore.QPoint(280, 170), QtCore.QPoint(20, 180),
                QtCore.QPoint(280, 180))
        painter.drawLines(QtCore.QPointF(20., 190.),
                QtCore.QPointF(280., 190.), QtCore.QPointF(20., 200.),
                QtCore.QPointF(280., 200.))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPainter")
    window.show()
    sys.exit(app.exec())
