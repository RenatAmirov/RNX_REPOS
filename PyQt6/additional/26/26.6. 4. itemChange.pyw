from PyQt6 import QtCore, QtWidgets, QtGui
import sys

GIC = QtWidgets.QGraphicsItem.GraphicsItemChange

class MyRect(QtWidgets.QGraphicsRectItem):
    def __init__(self, r):
        QtWidgets.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.darkGreen))
        self.setRect(r)

    def itemChange(self, signal, value):
        match signal:
            case GIC.ItemEnabledChange:
                print("ItemEnabledChange", value)
            case GIC.ItemEnabledHasChanged:
                print("ItemEnabledHasChanged", value)
            case GIC.ItemSelectedChange:
                print("ItemSelectedChange", value)
            case GIC.ItemSelectedHasChanged:
                print("ItemSelectedHasChanged", value)
            case GIC.ItemPositionChange:
                print("ItemPositionChange", value)
            case GIC.ItemPositionHasChanged:
                print("ItemPositionHasChanged", value)
            case GIC.ItemScenePositionHasChanged:
                print("ItemScenePositionHasChanged", value)
            case _:
                print("itemChange", signal)
        return QtWidgets.QGraphicsRectItem.itemChange(self, signal, value)

def on_clicked():
    view.setFocus()
    rect.setEnabled(not rect.isEnabled())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Обработка изменения состояния")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

rect = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 200.0))
rect.setPos(QtCore.QPointF(50.0, 50.0))
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
rect.setFlag(
     QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges)
rect.setFlag(
     QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemSendsScenePositionChanges)
scene.addItem(rect)

view = QtWidgets.QGraphicsView(scene)

button = QtWidgets.QPushButton("Переключить статус доступности")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec())
