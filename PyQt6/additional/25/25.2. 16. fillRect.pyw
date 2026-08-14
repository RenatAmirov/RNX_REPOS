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
        brush1 = QtGui.QBrush(QtCore.Qt.GlobalColor.green,
                              style=QtCore.Qt.BrushStyle.Dense5Pattern)
        painter.fillRect(50, 50, 80, 80, brush1)
        brush2 = QtGui.QBrush(QtCore.Qt.GlobalColor.green,
                              style=QtCore.Qt.BrushStyle.CrossPattern)
        painter.fillRect(QtCore.QRect(150, 50, 80, 80), brush2)
        brush3 = QtGui.QBrush(QtCore.Qt.GlobalColor.green,
                              style=QtCore.Qt.BrushStyle.DiagCrossPattern)
        painter.fillRect(QtCore.QRectF(50., 150., 80., 80.), brush3)
        painter.fillRect(QtCore.QRect(150, 150, 80, 80),
                         QtCore.Qt.GlobalColor.green)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPainter")
    window.show()
    sys.exit(app.exec())
