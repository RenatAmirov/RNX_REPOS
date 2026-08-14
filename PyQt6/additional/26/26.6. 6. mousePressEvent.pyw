from PyQt6 import QtCore, QtWidgets, QtGui
import sys

class MyRect(QtWidgets.QGraphicsRectItem):
    def __init__(self, r):
        QtWidgets.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.darkGreen))
        self.setRect(r)

    def mousePressEvent(self, e):
        print("mousePressEvent")
        e.accept()

    def mouseReleaseEvent(self, e):
        print("mouseReleaseEvent")
        QtWidgets.QGraphicsRectItem.mouseReleaseEvent(self, e)

    def mouseMoveEvent(self, e):
        print("mouseMoveEvent")
        QtWidgets.QGraphicsRectItem.mouseMoveEvent(self, e)
        
    def mouseDoubleClickEvent(self, e):
        print("mouseDoubleClickEvent")
        QtWidgets.QGraphicsRectItem.mouseDoubleClickEvent(self, e)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("События мыши")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

rect = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0))
rect.setPos(QtCore.QPointF(50.0, 150.0))
scene.addItem(rect)

view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
