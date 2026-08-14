from PyQt6 import QtCore, QtWidgets, QtGui
import sys

def on_clicked():
    scene.setSceneRect(0.0, 0.0, 600.0, 400.0)

def on_changed(arr):
    print("on_changed", arr)

def on_scene_rect_changed(r):
    print("on_scene_rect_changed", r)

def on_selection_changed():
    print("on_selection_changed")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

scene.changed.connect(on_changed)
scene.sceneRectChanged["QRectF"].connect(on_scene_rect_changed)
scene.selectionChanged.connect(on_selection_changed)

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

button = QtWidgets.QPushButton("Изменить размеры сцены")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec())
