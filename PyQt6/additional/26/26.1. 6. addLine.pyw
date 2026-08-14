from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(500, 300)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 475.0, 275.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

scene.addLine(50.0, 50.0, 450.0, 50.0,
              pen=QtGui.QPen(QtCore.Qt.GlobalColor.red, 3))
scene.addLine(QtCore.QLineF(50.0, 150.0, 450.0, 150.0), 
              pen=QtGui.QPen(QtCore.Qt.GlobalColor.blue, 3))

view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
