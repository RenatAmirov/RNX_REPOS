from PyQt6 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 410)
    
    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        black = QtCore.Qt.GlobalColor.black
        white = QtCore.Qt.GlobalColor.white
        red = QtCore.Qt.GlobalColor.red
        painter.setPen(QtGui.QPen(black))
        painter.setBrush(QtGui.QBrush(white))
        painter.drawRect(3, 3, 294, 404)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.SolidPattern))
        painter.drawRect(10, 10, 100, 30)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.Dense1Pattern))
        painter.drawRect(10, 50, 100, 30)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.Dense2Pattern))
        painter.drawRect(10, 90, 100, 30)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.Dense3Pattern))
        painter.drawRect(10, 130, 100, 30)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.Dense4Pattern))
        painter.drawRect(10, 170, 100, 30)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.Dense5Pattern))
        painter.drawRect(10, 210, 100, 30)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.Dense6Pattern))
        painter.drawRect(10, 250, 100, 30)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.Dense7Pattern))
        painter.drawRect(10, 290, 100, 30)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.CrossPattern))
        painter.drawRect(10, 330, 100, 30)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.HorPattern))
        painter.drawRect(10, 370, 100, 30)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.VerPattern))
        painter.drawRect(190, 10, 100, 30)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.BDiagPattern))
        painter.drawRect(190, 50, 100, 30)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.FDiagPattern))
        painter.drawRect(190, 90, 100, 30)
        painter.setBrush(QtGui.QBrush(red,
                         style=QtCore.Qt.BrushStyle.DiagCrossPattern))
        painter.drawRect(190, 130, 100, 30)
        gradient1 = QtGui.QLinearGradient(190, 185, 290, 185)
        gradient1.setColorAt(0, QtCore.Qt.GlobalColor.black)
        gradient1.setColorAt(0.5, QtCore.Qt.GlobalColor.white)
        gradient1.setColorAt(1, QtCore.Qt.GlobalColor.black)
        painter.setBrush(QtGui.QBrush(gradient1))
        painter.drawRect(190, 170, 100, 30)
        gradient2 = QtGui.QConicalGradient(240, 225, 0)
        gradient2.setColorAt(0, QtCore.Qt.GlobalColor.black)
        gradient2.setColorAt(0.5, QtCore.Qt.GlobalColor.white)
        gradient2.setColorAt(1, QtCore.Qt.GlobalColor.red)
        painter.setBrush(QtGui.QBrush(gradient2))
        painter.drawRect(190, 210, 100, 30)
        gradient3 = QtGui.QRadialGradient(240, 265, 70)
        gradient3.setColorAt(0, QtCore.Qt.GlobalColor.white)
        gradient3.setColorAt(1, QtCore.Qt.GlobalColor.red)
        painter.setBrush(QtGui.QBrush(gradient3))
        painter.drawRect(190, 250, 100, 30)
        ico = self.style().standardIcon(
                   QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical)
        painter.setBrush(QtGui.QBrush(ico.pixmap(QtCore.QSize(32, 32))))
        painter.drawRect(190, 290, 100, 30)
        brush = QtGui.QBrush(black)
        brush.setTexture(ico.pixmap(QtCore.QSize(16, 16)).mask())
        painter.setBrush(brush)
        painter.drawRect(190, 330, 100, 30)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QBrush")
    window.show()
    sys.exit(app.exec())
