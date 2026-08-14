from PyQt6 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(600, 400)
        self.pix = QtGui.QPixmap("photo.jpg", "JPG")
        mask = QtGui.QBitmap(self.pix.size())
        mask.clear()
        painter = QtGui.QPainter()
        painter.begin(mask)
        painter.setPen(QtCore.Qt.GlobalColor.color1)
        painter.setBrush(QtCore.Qt.GlobalColor.color1)
        painter.setFont(QtGui.QFont("Tahoma", 26, weight=75))
        painter.setRenderHint(QtGui.QPainter.RenderHint.TextAntialiasing)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.drawText(0, 0, 500, 50, 
                         QtCore.Qt.AlignmentFlag.AlignCenter,
                         "Камеронова галерея")
        painter.drawEllipse(50, 50, 400, 250)
        painter.end()
        self.pix.setMask(mask)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QBitmap")
    window.show()
    sys.exit(app.exec())
