from PyQt6 import QtCore, QtWidgets, QtGui
import sys

def on_clicked():
    r = view.viewport().rect()
    img = QtGui.QImage(int(r.width()), int(r.height()), 
                       QtGui.QImage.Format.Format_ARGB32_Premultiplied)
    img.fill(QtGui.QColor("#ffffff").rgb())
    painter = QtGui.QPainter()
    painter.begin(img)
    view.render(painter)
    painter.end()
    img.save("scene.png", "PNG")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsView")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

line1 = scene.addLine(50.0, 50.0, 450.0, 50.0, 
                      pen=QtGui.QPen(QtCore.Qt.GlobalColor.red, 3))
line1.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
line1.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
line1.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)

line2 = scene.addLine(QtCore.QLineF(50.0, 100.0, 450.0, 100.0), 
                      pen=QtGui.QPen(QtCore.Qt.GlobalColor.blue, 3))
line2.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
line2.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
line2.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)

rect = scene.addRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0), 
                     pen=QtGui.QPen(QtCore.Qt.GlobalColor.blue, 3),
                     brush=QtGui.QBrush(QtCore.Qt.GlobalColor.green))
rect.setPos(QtCore.QPointF(50.0, 150.0))
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)

view = QtWidgets.QGraphicsView(scene)

button = QtWidgets.QPushButton("Сохранить")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec())
