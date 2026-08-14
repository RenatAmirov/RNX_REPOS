from PyQt6 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 300)
        painter = QtGui.QPainter()
        self.pix = QtGui.QPixmap(300, 300)
        self.pix.fill(color=QtGui.QColor("#00ff00"))
        painter.begin(self.pix)
        black = QtCore.Qt.GlobalColor.black
        white = QtCore.Qt.GlobalColor.white
        red = QtCore.Qt.GlobalColor.red
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setPen(QtGui.QPen(black))
        painter.setBrush(QtGui.QBrush(white))
        painter.drawRect(3, 3, 294, 294)
        
        painter.setPen(QtGui.QPen(red, 2, style=QtCore.Qt.PenStyle.SolidLine))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.green,
                                style=QtCore.Qt.BrushStyle.Dense5Pattern))
        painter.drawRect(50, 50, 80, 80)
        painter.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.green,
                                style=QtCore.Qt.BrushStyle.CrossPattern))
        painter.drawRect(QtCore.QRect(150, 50, 80, 80))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.green,
                         style=QtCore.Qt.BrushStyle.DiagCrossPattern))
        painter.drawRect(QtCore.QRectF(50., 150., 80., 80.))
        painter.setPen(QtGui.QPen(red, 0, style=QtCore.Qt.PenStyle.NoPen))
        painter.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.green,
                                style=QtCore.Qt.BrushStyle.SolidPattern))
        painter.drawRect(QtCore.QRect(150, 150, 80, 80))
        painter.end()

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPixmap")
    window.show()
    sys.exit(app.exec())
