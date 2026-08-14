from PyQt6 import QtWidgets, QtGui
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Содержимое страницы")
        self.button = QtWidgets.QPushButton("Отобразить сообщение в трее")
        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.label)
        self.box.addWidget(self.button)
        self.setLayout(self.box)

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        ico = self.style().standardIcon(
                   QtWidgets.QStyle.StandardPixmap.SP_ComputerIcon)
        self.w = MyWidget()
        self.setCentralWidget(self.w)
        self.w.button.clicked.connect(self.on_clicked)
        self.add_menu()
        self.sys_tray = QtWidgets.QSystemTrayIcon(ico, self)
        self.sys_tray.setToolTip("Описание программы")
        self.on_create_context_menu()
        self.sys_tray.activated.connect(self.on_activated)
        self.sys_tray.messageClicked.connect(self.on_messageClicked)
        self.sys_tray.show()

    def add_menu(self):
        self.menuFile = QtWidgets.QMenu("&File")
        self.actExit = QtGui.QAction("&Exit", None)
        self.actExit.triggered.connect(
                     QtWidgets.QApplication.instance().quit)
        self.menuFile.addAction(self.actExit)
        self.menuBar().addMenu(self.menuFile)

    def on_create_context_menu(self):
        self.menuSystemTray = QtWidgets.QMenu("&SystemTray")
        self.actShowHide = QtGui.QAction("&Отобразить или скрыть окно", None)
        self.actShowHide.triggered.connect(self.on_show_hide)
        self.menuSystemTray.addAction(self.actShowHide)
        
        self.menuSystemTray.addSeparator()
        
        self.actQuit = QtGui.QAction("&Выход", None)
        self.actQuit.triggered.connect(
                     QtWidgets.QApplication.instance().quit)
        self.menuSystemTray.addAction(self.actQuit)
        
        self.sys_tray.setContextMenu(self.menuSystemTray)

    def closeEvent(self, e):
        self.hide()
        e.ignore()

    def on_clicked(self):
        self.sys_tray.showMessage("Название", "Текст сообщения",
                                  msecs=2000)

    def on_show_hide(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.activateWindow()

    def on_activated(self, st):
        print("on_activated", st)

    def on_messageClicked(self):
        print("on_messageClicked")

app = QtWidgets.QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)
window = MyWindow()
window.setWindowTitle("Класс QSystemTrayIcon")
window.resize(700, 350)
window.show()
sys.exit(app.exec())
