from PyQt6 import QtCore, QtWidgets, QtGui
import sys

class MyRect(QtWidgets.QGraphicsRectItem):
    def __init__(self, r):
        QtWidgets.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.darkGreen))
        self.setRect(r)
        self.setFlag(
                QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)

    def focusInEvent(self, e):
        self.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.red, 3))
        QtWidgets.QGraphicsRectItem.focusInEvent(self, e)

    def focusOutEvent(self, e):
        self.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.black, 3))
        QtWidgets.QGraphicsRectItem.focusOutEvent(self, e)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key.Key_Up:
            self.moveBy(0, -5)
        elif e.key() == QtCore.Qt.Key.Key_Down:
            self.moveBy(0, 5)
        elif e.key() == QtCore.Qt.Key.Key_Left:
            self.moveBy(-5, 0)
        elif e.key() == QtCore.Qt.Key.Key_Right:
            self.moveBy(5, 0)
        e.ignore()
        QtWidgets.QGraphicsRectItem.keyPressEvent(self, e)
        
    def keyReleaseEvent(self, e):
        QtWidgets.QGraphicsRectItem.keyReleaseEvent(self, e)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Обработка событий клавиатуры")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

rect = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0))
rect.setPos(QtCore.QPointF(50.0, 150.0))
scene.addItem(rect)

rect2 = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 50.0))
rect2.setPos(QtCore.QPointF(50.0, 50.0))
scene.addItem(rect2)
rect.setFocusProxy(rect2)

view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
