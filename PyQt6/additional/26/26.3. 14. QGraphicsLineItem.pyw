from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsLineItem")
window.resize(600, 600)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

line = QtWidgets.QGraphicsLineItem(50, 50, 450, 450)
line.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.darkBlue, 3))
line.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
line.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
line.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
scene.addItem(line)

view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
