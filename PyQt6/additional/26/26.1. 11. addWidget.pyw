from PyQt6 import QtCore, QtWidgets, QtGui
import sys

def on_clicked():
    print("Нажата кнопка")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QGraphicsScene")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.GlobalColor.white)

w = QtWidgets.QWidget()
w.move(50, 50)
w.resize(300, 50)
btn = QtWidgets.QPushButton("Командная кнопка")
btn.clicked.connect(on_clicked)
b = QtWidgets.QVBoxLayout()
b.addWidget(btn)
w.setLayout(b)
widget1 = scene.addWidget(w, QtCore.Qt.WindowType.Window)
widget1.setWindowTitle("Заголовок окна 1")

w2 = QtWidgets.QWidget()
w2.move(50, 250)
w2.resize(300, 50)
widget2 = scene.addWidget(w2, QtCore.Qt.WindowType.Window)
widget2.setWindowTitle("Заголовок окна 2")

view = QtWidgets.QGraphicsView(scene)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)

window.show()
scene.setActiveWindow(widget2)
sys.exit(app.exec())
