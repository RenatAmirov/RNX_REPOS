from PyQt6 import QtCore, QtWidgets, QtGui
import sys

class MyRect(QtWidgets.QGraphicsRectItem):
    def __init__(self, r):
        QtWidgets.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.darkGreen))
        self.setRect(r)
        self.setAcceptHoverEvents(True)

    def hoverEnterEvent(self, e):
        print("hoverEnterEvent")
        print("pos()", e.pos())
        print("scenePos()", e.scenePos())
        print("screenPos()", e.screenPos())
        print("lastPos()", e.lastPos())
        print("lastScenePos()", e.lastScenePos())
        print("lastScreenPos()", e.lastScreenPos())
        modifiers = []
        if e.modifiers() & QtCore.Qt.KeyboardModifier.ShiftModifier:
            modifiers.append("Shift")
        if e.modifiers() & QtCore.Qt.KeyboardModifier.ControlModifier:
            modifiers.append("Ctrl")
        if e.modifiers() & QtCore.Qt.KeyboardModifier.AltModifier:
            modifiers.append("Alt")
        if len(modifiers) == 0:
            modifiers.append("No")
        print("+".join(modifiers))
        self.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.red, 3))
        QtWidgets.QGraphicsRectItem.hoverEnterEvent(self, e)

    def hoverLeaveEvent(self, e):
        print("hoverLeaveEvent")
        self.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.black, 3))
        QtWidgets.QGraphicsRectItem.hoverLeaveEvent(self, e)

    def hoverMoveEvent(self, e):
        print("hoverMoveEvent")
        QtWidgets.QGraphicsRectItem.hoverMoveEvent(self, e)

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
