from PyQt6 import QtCore, QtWidgets, QtGui
import sys

class MyRect(QtWidgets.QGraphicsRectItem):
    def __init__(self, r):
        QtWidgets.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.darkGreen))
        self.setRect(r)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat("text/plain"):
            e.acceptProposedAction()

    def dropEvent(self, e):
        if e.mimeData().hasFormat("text/plain"):
            txt.setText(str(e.mimeData().data("text/plain"), "utf-8"))
            e.accept()
        else:
            e.ignore()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("События перетаскивания и сброса")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

rect = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 200.0))
rect.setPos(QtCore.QPointF(50.0, 50.0))
scene.addItem(rect)

txt = scene.addSimpleText("Перетащите сюда текст", 
                          QtGui.QFont("Verdana", 16))
txt.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.white, 1))
txt.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.white))
txt.setParentItem(rect)
txt.setPos(20.0, 80.0)

view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
