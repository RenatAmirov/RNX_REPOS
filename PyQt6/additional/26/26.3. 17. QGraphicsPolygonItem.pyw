from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsPolygonItem")
window.resize(600, 600)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

item = QtWidgets.QGraphicsPolygonItem(QtGui.QPolygonF([
                    QtCore.QPointF(50.0, 50.0),
                    QtCore.QPointF(450.0, 50.0),
                    QtCore.QPointF(250.0, 250.0)]))
item.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.darkBlue, 3))
item.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.darkGreen))
item.setPos(QtCore.QPointF(10.0, 150.0))
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
