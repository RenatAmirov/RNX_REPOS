from PyQt6 import QtCore, QtWidgets, QtGui
import sys

class MyRect(QtWidgets.QGraphicsRectItem):
    def __init__(self, r):
        QtWidgets.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.darkGreen))
        self.setRect(r)

    def wheelEvent(self, e):
        print("wheelEvent")
        print("delta()", e.delta())
        if e.orientation() == QtCore.Qt.Orientation.Horizontal:
            print("Колесико повернуто по горизонтали")
        elif e.orientation() == QtCore.Qt.Orientation.Vertical:
            print("Колесико повернуто по вертикали")
        if e.buttons() & QtCore.Qt.MouseButton.LeftButton:
            print("Нажата левая кнопка мыши")
        if e.buttons() & QtCore.Qt.MouseButton.RightButton:
            print("Нажата правая кнопка мыши")
        if e.buttons() & QtCore.Qt.MouseButton.MiddleButton:
            print("Нажата средняя кнопка мыши")
        if (e.buttons() & QtCore.Qt.MouseButton.LeftButton and 
            e.buttons() & QtCore.Qt.MouseButton.RightButton):
            print("Левая и правая кнопки нажаты")
        print("pos()", e.pos())
        print("scenePos()", e.scenePos())
        print("screenPos()", e.screenPos())
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
        QtWidgets.QGraphicsRectItem.wheelEvent(self, e)

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
