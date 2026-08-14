from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsTextItem")
window.resize(600, 600)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

item = QtWidgets.QGraphicsTextItem()
item.setHtml("<u>Редактируемый <b>текст</b></u>")
item.setDefaultTextColor(QtCore.Qt.GlobalColor.darkBlue)
item.setFont(QtGui.QFont("Verdana", 16))
item.setPos(QtCore.QPointF(50.0, 150.0))
item.setTextWidth(300)
item.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextEditorInteraction)
item.setTabChangesFocus(False)

item.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
item.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
item.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
scene.addItem(item)

print(item.toHtml(), item.toPlainText())
view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
sys.exit(app.exec())
