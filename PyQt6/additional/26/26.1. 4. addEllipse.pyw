from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(500, 300)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 475.0, 275.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

e1 = scene.addEllipse(0.0, 0.0, 400.0, 100.0, 
              pen=QtGui.QPen(QtCore.Qt.GlobalColor.red, 3),
              brush=QtGui.QBrush(QtCore.Qt.GlobalColor.yellow))
e1.setPos(QtCore.QPointF(50.0, 30.0))
e2 = scene.addEllipse(QtCore.QRectF(0.0, 0.0, 400.0, 100.0), 
              pen=QtGui.QPen(QtCore.Qt.GlobalColor.blue, 3),
              brush=QtGui.QBrush(QtCore.Qt.GlobalColor.green))
e2.setPos(QtCore.QPointF(50.0, 150.0))
view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
