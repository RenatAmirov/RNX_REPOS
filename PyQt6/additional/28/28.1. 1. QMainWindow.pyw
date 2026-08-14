from PyQt6 import QtCore, QtWidgets, QtGui
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Содержимое страницы")
        self.button = QtWidgets.QPushButton("Кнопка")
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
        self.setToolButtonStyle(
                    QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.setIconSize(QtCore.QSize(32, 32))
        #self.setAnimated(False)
        self.setDockOptions(
                QtWidgets.QMainWindow.DockOption.AnimatedDocks | 
                QtWidgets.QMainWindow.DockOption.AllowTabbedDocks)
        self.setTabPosition(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea,
                            QtWidgets.QTabWidget.TabPosition.North)
        self.setTabPosition(QtCore.Qt.DockWidgetArea.RightDockWidgetArea,
                            QtWidgets.QTabWidget.TabPosition.North)
        self.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.add_menu()
        self.add_tool_bar()
        self.add_dock_widget()
        self.statusBar().showMessage("Текст в строке состояния")

    def add_menu(self):
        self.menuFile = QtWidgets.QMenu("&File")
        self.actOpen = QtGui.QAction("Open", None)
        self.actOpen.setShortcut(QtGui.QKeySequence.StandardKey.Open)
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)
        self.menuBar().addMenu(self.menuFile)

    def add_tool_bar(self):
        self.toolBar = QtWidgets.QToolBar("MyToolBar")
        ico = self.style().standardIcon(
                   QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical)
        self.actClose = self.toolBar.addAction(ico, "Close",
                             QtWidgets.QApplication.instance().quit)
        self.actClose.setShortcut(QtGui.QKeySequence.StandardKey.Close)
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        #self.addToolBarBreak(QtCore.Qt.TopToolBarArea)
        self.toolBar2 = QtWidgets.QToolBar("MyToolBar2")
        ico2 = self.style().standardIcon(
                    QtWidgets.QStyle.StandardPixmap.SP_DialogCloseButton)
        self.actQuit = self.toolBar2.addAction(ico2, "Quit",
                            QtWidgets.QApplication.instance().quit)
        self.actQuit.setShortcut(QtGui.QKeySequence.StandardKey.Quit)
        #self.insertToolBar(self.toolBar, self.toolBar2)
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar2)
        #self.insertToolBarBreak(self.toolBar2)

    def add_dock_widget(self):
        self.dw = QtWidgets.QDockWidget("MyDockWidget1")
        self.lbl = QtWidgets.QLabel("Содержимое панели 1")
        self.lbl.setWordWrap(True)
        self.lbl.setFrameStyle(
             QtWidgets.QFrame.Shape.Box | QtWidgets.QFrame.Shadow.Plain)
        self.dw.setWidget(self.lbl)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea,
                           self.dw)
        
        self.dw2 = QtWidgets.QDockWidget("MyDockWidget2")
        self.lbl2 = QtWidgets.QLabel("Содержимое панели 2")
        self.lbl2.setWordWrap(True)
        self.lbl2.setFrameStyle(
            QtWidgets.QFrame.Shape.Box | QtWidgets.QFrame.Shadow.Plain)
        self.dw2.setWidget(self.lbl2)
        self.addDockWidget(QtCore.Qt.DockWidgetArea.LeftDockWidgetArea,
                           self.dw2, QtCore.Qt.Orientation.Vertical)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_clicked(self):
        print("Нажата кнопка")

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QMainWindow")
window.resize(500, 350)

window.show()
sys.exit(app.exec())
