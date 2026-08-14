from PyQt6 import QtCore, QtWidgets, QtGui
import sys

def on_clicked():
    view.setFocus()
    effect.setEnabled(not effect.isEnabled())
    effect.setOpacityMask(QtGui.QBrush(QtCore.Qt.BrushStyle.CrossPattern))
    effect.setOpacity(0.3)

def on_enabled_changed(status):
    print("on_enabled_changed", status)

def on_opacity_changed(opacity):
    print("on_opacity_changed", opacity)

def on_mask_changed(mask):
    print("on_mask_changed")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsOpacityEffect")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

rect = scene.addRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0), 
                     pen=QtGui.QPen(QtCore.Qt.GlobalColor.red, 3),
                     brush=QtGui.QBrush(QtCore.Qt.GlobalColor.darkGreen))
rect.setPos(QtCore.QPointF(50.0, 150.0))
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)

effect = QtWidgets.QGraphicsOpacityEffect()
effect.setOpacity(0.5)
effect.enabledChanged[bool].connect(on_enabled_changed)
effect.opacityMaskChanged["QBrush"].connect(on_mask_changed)
effect.opacityChanged["qreal"].connect(on_opacity_changed)
rect.setGraphicsEffect(effect)

view = QtWidgets.QGraphicsView(scene)

button = QtWidgets.QPushButton("Переключить статус и изменить параметры")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec())
