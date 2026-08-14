from PyQt6 import QtCore, QtWidgets, QtGui
import sys

class MyRect(QtWidgets.QGraphicsRectItem):
    def __init__(self, r, n):
        QtWidgets.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.darkGreen))
        self.setRect(r)
        self.n = n

    def mousePressEvent(self, e):
        print("mousePressEvent", self.n)
        e.accept()

    def mouseReleaseEvent(self, e):
        print("mouseReleaseEvent", self.n)
        QtWidgets.QGraphicsRectItem.mouseReleaseEvent(self, e)

    def mouseMoveEvent(self, e):
        print("mouseMoveEvent", self.n)
        QtWidgets.QGraphicsRectItem.mouseMoveEvent(self, e)
        
    def mouseDoubleClickEvent(self, e):
        print("mouseDoubleClickEvent", self.n)
        QtWidgets.QGraphicsRectItem.mouseDoubleClickEvent(self, e)

    def sceneEventFilter(self, item, e):
        print("*" * 30)
        print("sceneEventFilter", self.n)
        return False

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Фильтрация событий")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

rect = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 200.0), 1)
rect.setPos(QtCore.QPointF(50.0, 50.0))
scene.addItem(rect)

rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

rect2 = MyRect(QtCore.QRectF(0.0, 0.0, 300.0, 100.0), 2)
rect2.setPos(QtCore.QPointF(10.0, 10.0))
rect2.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.yellow))
rect2.setParentItem(rect)
rect2.installSceneEventFilter(rect)

view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
