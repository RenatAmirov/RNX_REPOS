from PyQt6 import QtCore, QtWidgets, QtGui
import sys

def on_clicked():
    view.setFocus()
    effect.setEnabled(not effect.isEnabled())
    effect.setColor(QtGui.QColor(255, 0, 0, 180))
    effect.setBlurRadius(50)
    effect.setXOffset(10)

def on_enabled_changed(status):
    print("on_enabled_changed", status)
    
def on_color_changed(color):
    print("on_color_changed", color.getRgb())
    
def on_blur_changed(b):
    print("on_blur_changed", b)

def on_offset_changed(offset):
    print("on_offset_changed", offset)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsDropShadowEffect")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

rect = scene.addRect(QtCore.QRectF(0.0, 0.0, 400.0, 100.0), 
                     pen=QtGui.QPen(QtCore.Qt.GlobalColor.darkGreen, 1),
                     brush=QtGui.QBrush(QtCore.Qt.GlobalColor.darkGreen))
rect.setPos(QtCore.QPointF(50.0, 150.0))
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
rect.setFlag(QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)

effect = QtWidgets.QGraphicsDropShadowEffect()
effect.setColor(QtGui.QColor(128, 128, 128, 180))
effect.setBlurRadius(30)
effect.setXOffset(20)
effect.setYOffset(20)
effect.enabledChanged["bool"].connect(on_enabled_changed)
effect.colorChanged["const QColor&"].connect(on_color_changed)
effect.blurRadiusChanged["qreal"].connect(on_blur_changed)
effect.offsetChanged["const QPointF&"].connect(on_offset_changed)
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
