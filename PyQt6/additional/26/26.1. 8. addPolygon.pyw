from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(500, 300)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 475.0, 275.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

scene.addPolygon(QtGui.QPolygonF([
                    QtCore.QPointF(50.0, 50.0),
                    QtCore.QPointF(450.0, 50.0),
                    QtCore.QPointF(250.0, 250.0)]), 
                 pen=QtGui.QPen(QtCore.Qt.GlobalColor.red, 3),
                 brush=QtGui.QBrush(QtCore.Qt.GlobalColor.yellow))

view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
