from PyQt6 import QtCore, QtWidgets, QtGui
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Содержимое страницы")
        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.label)
        self.setLayout(self.box)

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.w = MyWidget()
        self.setCentralWidget(self.w)
        self.add_tool_bar()
        self.statusBar().showMessage("")

    def add_tool_bar(self):
        self.toolBar = QtWidgets.QToolBar("MyToolBar")
        self.actH = QtGui.QAction("&Help", self)
        ico2 = self.style().standardIcon(
                    QtWidgets.QStyle.StandardPixmap.SP_MessageBoxInformation)
        self.actH.setIcon(ico2)
        self.actH.setShortcut("F1")
        self.toolBar.addAction(self.actH)
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QToolBar")
window.resize(500, 350)
window.show()
sys.exit(app.exec())
