from PyQt6 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(600, 600)
        self.pix = QtGui.QPixmap("photo.jpg", "JPG")
        self.pix = self.pix.scaled(300, 600, 
             aspectRatioMode=QtCore.Qt.AspectRatioMode.IgnoreAspectRatio,
             transformMode=QtCore.Qt.TransformationMode.FastTransformation)
    
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
