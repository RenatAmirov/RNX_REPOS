from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsPixmapItem")
window.resize(600, 600)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

pix = QtGui.QPixmap("photo.jpg")
mask = QtGui.QBitmap(pix.size())
mask.clear()
painter = QtGui.QPainter()
painter.begin(mask)
painter.setPen(QtCore.Qt.GlobalColor.color1)
painter.setBrush(QtCore.Qt.GlobalColor.color1)
painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
painter.drawEllipse(50, 50, 400, 250)
painter.end()
pix.setMask(mask)

item = QtWidgets.QGraphicsPixmapItem()
item.setPixmap(pix)
item.setOffset(50, 50)
item.setShapeMode(QtWidgets.QGraphicsPixmapItem.MaskShape)

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
