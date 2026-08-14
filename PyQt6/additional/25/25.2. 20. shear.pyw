from PyQt6 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 300)
    
    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        black = QtCore.Qt.GlobalColor.black
        white = QtCore.Qt.GlobalColor.white
        painter.setPen(QtGui.QPen(black))
        painter.setBrush(QtGui.QBrush(white))
        painter.drawRect(3, 3, 294, 294)
        
        painter.fillRect(10, 10, 50, 50, QtCore.Qt.GlobalColor.red)
        painter.save()
        painter.shear(0.2, 0.2)
        painter.fillRect(80, 80, 50, 50, QtCore.Qt.GlobalColor.green)
        painter.restore()
        painter.fillRect(150, 150, 50, 50, QtCore.Qt.GlobalColor.blue)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPainter")
    window.show()
    sys.exit(app.exec())
