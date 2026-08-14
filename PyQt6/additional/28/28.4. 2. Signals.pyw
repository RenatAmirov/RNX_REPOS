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
        self.dw.dockLocationChanged.connect(self.on_dockLocationChanged)
        self.dw.topLevelChanged[bool].connect(self.on_topLevelChanged)
        self.dw.visibilityChanged[bool].connect(self.on_visibilityChanged)
        self.lbl = QtWidgets.QLabel("Содержимое панели 1")
        self.lbl.setWordWrap(True)
        self.lbl.setFrameStyle(
             QtWidgets.QFrame.Shape.Box | QtWidgets.QFrame.Shadow.Plain)
        self.dw.setWidget(self.lbl)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea,
                           self.dw)
        

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_dockLocationChanged(self, area):
        match area:
            case QtCore.Qt.DockWidgetArea.LeftDockWidgetArea:
                print("Область слева")
            case QtCore.Qt.DockWidgetArea.RightDockWidgetArea:
                print("Область справа")
            case QtCore.Qt.DockWidgetArea.TopDockWidgetArea:
                print("Область сверху")
            case QtCore.Qt.DockWidgetArea.BottomDockWidgetArea:
                print("Область снизу")
            case _:
                print("Панель не прикреплена")

    def on_topLevelChanged(self, status):
        print("on_topLevelChanged", status)

    def on_visibilityChanged(self, status):
        print("visibilityChanged", status)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QDockWidget")
window.resize(500, 350)

window.show()
sys.exit(app.exec())
