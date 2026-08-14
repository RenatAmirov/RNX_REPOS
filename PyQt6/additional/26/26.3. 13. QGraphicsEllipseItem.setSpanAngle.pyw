from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsEllipseItem")
window.resize(600, 600)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

item = QtWidgets.QGraphicsEllipseItem()
item.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.darkBlue, 3))
item.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.darkGreen))
item.setRect(0.0, 0.0, 400.0, 400.0)
item.setPos(QtCore.QPointF(50.0, 50.0))
item.setStartAngle(0)
item.setSpanAngle(-90 * 16)

item.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
item.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
item.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
scene.addItem(item)

view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
