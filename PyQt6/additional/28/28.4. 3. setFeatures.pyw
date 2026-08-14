from PyQt6 import QtCore, QtWidgets, QtGui
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Содержимое страницы")
        self.button = QtWidgets.QPushButton(
             "Удалить все свойства панели 4")
        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.label)
        self.box.addWidget(self.button)
        self.setLayout(self.box)

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.w = MyWidget()
        self.setCentralWidget(self.w)
        self.w.button.clicked.connect(self.on_clicked)
        #self.setAnimated(False)
        self.add_menu()
        self.add_dock_widget()

    def add_menu(self):
        self.menuFile = QtWidgets.QMenu("&File")
        self.actOpen = QtGui.QAction("Open", None)
        self.actOpen.setShortcut(QtGui.QKeySequence.StandardKey.Open)
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)
        self.menuBar().addMenu(self.menuFile)

    def add_dock_widget(self):
        self.dw = QtWidgets.QDockWidget("MyDockWidget1")
        self.dw.setFeatures(
                QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetClosable)
        self.lbl = QtWidgets.QLabel("Содержимое панели 1")
        self.lbl.setWordWrap(True)
        self.lbl.setFrameStyle(
             QtWidgets.QFrame.Shape.Box | QtWidgets.QFrame.Shadow.Plain)
        self.dw.setWidget(self.lbl)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea,
                           self.dw)
        
        self.dw2 = QtWidgets.QDockWidget("MyDockWidget2")
        self.dw2.setFeatures(
                 QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetClosable |
                 QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.lbl2 = QtWidgets.QLabel("Содержимое панели 2")
        self.lbl2.setWordWrap(True)
        self.lbl2.setFrameStyle(
             QtWidgets.QFrame.Shape.Box | QtWidgets.QFrame.Shadow.Plain)
        self.dw2.setWidget(self.lbl2)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.TopDockWidgetArea,
                           self.dw2)

        self.dw3 = QtWidgets.QDockWidget("MyDockWidget3")
        self.dw3.setFeatures(
                 QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetClosable |
                 QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable |
                 QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFloatable)
        self.lbl3 = QtWidgets.QLabel("Содержимое панели 3")
        self.lbl3.setWordWrap(True)
        self.lbl3.setFrameStyle(
             QtWidgets.QFrame.Shape.Box | QtWidgets.QFrame.Shadow.Plain)
        self.dw3.setWidget(self.lbl3)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.RightDockWidgetArea,
                           self.dw3)
        
        self.dw4 = QtWidgets.QDockWidget("MyDockWidget4")
        self.dw4.setFeatures(
             QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetClosable |
             QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable |
             QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFloatable |
             QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetVerticalTitleBar)
        self.lbl4 = QtWidgets.QLabel("Содержимое панели 4")
        self.lbl4.setWordWrap(True)
        self.lbl4.setFrameStyle(
             QtWidgets.QFrame.Shape.Box | QtWidgets.QFrame.Shadow.Plain)
        self.dw4.setWidget(self.lbl4)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.BottomDockWidgetArea,
                           self.dw4)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_clicked(self):
        self.dw4.setFeatures(
             QtWidgets.QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QDockWidget")
window.resize(500, 350)

window.show()
sys.exit(app.exec())
