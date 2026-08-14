from PyQt6 import QtCore, QtWidgets, QtGui
import sys

class MyItem(QtWidgets.QGraphicsItem):
    pen_width = 1
    def boundingRect(self):
        return QtCore.QRectF(-200 - MyItem.pen_width,
                      -100 - MyItem.pen_width, 400 + MyItem.pen_width * 2,
                      200 + MyItem.pen_width * 2)

    def paint(self, painter, option, widget):
        painter.save()
        painter.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.red,
                                  MyItem.pen_width))
        painter.setBrush(QtCore.Qt.GlobalColor.darkGreen)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.drawEllipse(-200, -100, 400, 200)
        painter.restore()

    def shape(self):
        path = QtGui.QPainterPath()
        path.addEllipse(-200, -100, 400, 200)
        return path

def on_clicked():
    if my_item.isEnabled():
        my_item.setEnabled(False)
    else:
        my_item.setEnabled(True)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsItem")
window.resize(600, 600)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

rect = scene.addRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0), 
                     pen=QtGui.QPen(QtCore.Qt.GlobalColor.blue, 3),
                     brush=QtGui.QBrush(QtCore.Qt.GlobalColor.green))
rect.setPos(QtCore.QPointF(50.0, 150.0))
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)

my_item = MyItem()
my_item.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
my_item.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
my_item.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
my_item.setPos(250, 380)
my_item.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
scene.addItem(my_item)

view = QtWidgets.QGraphicsView(scene)

button = QtWidgets.QPushButton("Сделать доступным или недоступным")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec())
