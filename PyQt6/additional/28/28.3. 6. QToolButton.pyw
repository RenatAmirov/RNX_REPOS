from PyQt6 import QtCore, QtWidgets, QtGui
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Содержимое страницы")
        self.button = QtWidgets.QPushButton(
            "Проверить положение панели")
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
        self.toolBtn1 = self.toolBar.widgetForAction(self.actOpen)
        self.toolBtn1.setAutoRaise(False)
        
        self.actQuit = QtGui.QAction("Quit", None)
        ico = self.style().standardIcon(
                   QtWidgets.QStyle.StandardPixmap.SP_DialogCloseButton)
        self.actQuit.setIcon(ico)
        self.actQuit.setToolTip("Выход из приложения")
        self.actQuit.triggered.connect(self.on_quit)

        self.menuHelp = QtWidgets.QMenu("&Help")
        self.actHelp = QtGui.QAction("Help", None)
        self.actHelp.setShortcut("F1")
        self.actHelp.triggered.connect(self.on_help)
        self.menuHelp.addAction(self.actHelp)
        
        self.toolBtn2 = QtWidgets.QToolButton()
        self.toolBtn2.setDefaultAction(self.actQuit)
        self.toolBtn2.setMenu(self.menuHelp)
        #self.toolBtn2.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.toolBtn2.setPopupMode(
                 QtWidgets.QToolButton.ToolButtonPopupMode.MenuButtonPopup)
        #self.toolBtn2.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        #self.toolBtn2.setArrowType(QtCore.Qt.ArrowType.DownArrow)
        self.toolBtn2.triggered.connect(self.on_triggered)
        
        self.toolBar.addWidget(self.toolBtn2)
        

        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)

    def on_open(self):
        print("Выбран пункт меню Open")

    def on_quit(self):
        print("Нажата кнопка Quit")

    def on_help(self):
        print("Выбран пункт меню Help")

    def on_triggered(self, act):
        print("Выбрано дейстие", act.text())

    def on_clicked(self):
        print(self.toolBar.isFloating())

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Класс QToolButton")
window.resize(500, 350)

window.show()
sys.exit(app.exec())
