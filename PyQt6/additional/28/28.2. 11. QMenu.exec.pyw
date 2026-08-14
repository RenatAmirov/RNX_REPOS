from PyQt6 import QtWidgets, QtGui
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Содержимое страницы")
        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.label)
        self.setLayout(self.box)

    def contextMenuEvent(self, event):
        act1 = QtGui.QAction("Пункт &1", self)
        act1.triggered.connect(self.on_act1)
        act2 = QtGui.QAction("Пункт &2", self)
        act2.triggered.connect(self.on_act2)
        QtWidgets.QMenu.exec([act1, act2], event.globalPos(), at=act2,
                             parent=self)

    def on_act1(self):
        print("on_act1")

    def on_act2(self):
        print("on_act2")

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.w = MyWidget()
        self.setCentralWidget(self.w)
 
app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QMenu")
window.resize(500, 350)

window.show()
sys.exit(app.exec())
