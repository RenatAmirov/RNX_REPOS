from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Содержимое страницы")
        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.label)
        self.setLayout(self.box)
        self.cont_menu = QtWidgets.QMenu(self)
        self.cont_menu.addAction("Пункт &1", self.on_act1)
        self.cont_menu.addAction("Пункт &2", self.on_act2)

    def contextMenuEvent(self, e):
        self.cont_menu.exec(e.globalPos())

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
