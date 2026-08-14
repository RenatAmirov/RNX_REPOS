from PyQt6 import QtCore, QtWidgets, QtGui
import sys

def on_link_activated(s):
    print("on_link_activated", s)

def on_link_hovered(s):
    print("on_link_hovered", s)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsTextItem")
window.resize(600, 600)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 535.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

item = QtWidgets.QGraphicsTextItem()
item.setHtml('<a href="https://www.google.ru/">Это гиперссылка</a>')
item.setDefaultTextColor(QtCore.Qt.GlobalColor.darkBlue)
item.setFont(QtGui.QFont("Verdana", 16))
item.setPos(QtCore.QPointF(50.0, 150.0))
item.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextBrowserInteraction)
item.setOpenExternalLinks(True)
item.linkActivated[str].connect(on_link_activated)
item.linkHovered[str].connect(on_link_hovered)

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
