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
        self.add_menu()
        self.add_tool_bar()

    def add_menu(self):
        self.menuFile = QtWidgets.QMenu("&File")
        self.actOpen = QtGui.QAction("Open", None)
        ico = self.style().standardIcon(
                   QtWidgets.QStyle.StandardPixmap.SP_ComputerIcon)
        self.actOpen.setIcon(ico)
        self.actOpen.setShortcut(QtGui.QKeySequence.StandardKey.Open)
        self.actOpen.triggered.connect(self.on_open)
        self.menuFile.addAction(self.actOpen)
        self.menuBar().addMenu(self.menuFile)

    def add_tool_bar(self):
        self.toolBar = QtWidgets.QToolBar("MyToolBar")
        self.toolBar.addAction(self.actOpen)
        self.toolBar.addAction("1")
        ico = self.style().standardIcon(
                   QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical)
        self.toolBar.addAction(ico, "2")
        self.toolBar.addAction("Close1",
                               QtWidgets.QApplication.instance().quit)
        self.toolBar.addAction("Close2",
                               QtWidgets.QApplication.instance().quit)
        self.toolBar.addAction(ico, "Close3",
                               QtWidgets.QApplication.instance().quit)
        a = self.toolBar.addAction(ico, "Close4",
                                   QtWidgets.QApplication.instance().quit)
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.addToolBarBreak(QtCore.Qt.ToolBarArea.TopToolBarArea)
        
        self.toolBar2 = QtWidgets.QToolBar("MyToolBar2")
        ico2 = self.style().standardIcon(
                    QtWidgets.QStyle.StandardPixmap.SP_DialogCloseButton)
        self.actQuit = self.toolBar2.addAction(ico2, "Quit",
                                QtWidgets.QApplication.instance().quit)
        self.actQuit.setShortcut(QtGui.QKeySequence.StandardKey.Quit)
        
        self.act1 = QtGui.QAction(ico, "Пункт &1", self)
        self.act2 = QtGui.QAction(ico, "Пункт &2", self)
        self.act3 = QtGui.QAction(ico, "Пункт &3", self)
        self.act4 = QtGui.QAction(ico, "Пункт &4", self)
        
        self.toolBar2.addActions([self.act1, self.act2,
                                  self.act3, self.act4])
        
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar2)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_clicked(self):
        print("Нажата кнопка")

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QToolBar")
window.resize(500, 350)

window.show()
sys.exit(app.exec())
