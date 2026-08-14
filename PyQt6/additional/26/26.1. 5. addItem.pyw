from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(500, 300)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 475.0, 275.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

ellipse = QtWidgets.QGraphicsEllipseItem(0.0, 0.0, 300.0, 100.0)
ellipse.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.red, 3))
ellipse.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.yellow))
ellipse.setPos(QtCore.QPointF(50.0, 50.0))
scene.addItem(ellipse)

view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
