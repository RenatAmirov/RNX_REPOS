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
        
        font = QtGui.QFont("Tahoma", 16)
        fm = QtGui.QFontMetrics(font)
        print(fm.horizontalAdvance("Строка"))        # 67
        print(fm.height())                           # 25
        print(fm.boundingRect("Строка"))
                     # PyQt6.QtCore.QRect(0, -21, 66, 25)
        
        painter.setFont(font)
        painter.drawText(50, 50, "Строка")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QFont")
    window.show()
    sys.exit(app.exec())
