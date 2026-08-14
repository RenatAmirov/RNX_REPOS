from PyQt6 import QtCore, QtWidgets, QtWebEngineCore, QtWebEngineWidgets
import sys

def showNumberOfMatches(res):
    print("Количество совпадений:", res.numberOfMatches())

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window)
        self.setWindowTitle("Класс QWebEngineView")
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        self.chkWithCase = QtWidgets.QCheckBox("&С учётом регистра")
        hbox.addWidget(self.chkWithCase)
        self.txtFind = QtWidgets.QLineEdit()
        hbox.addWidget(self.txtFind)
        self.btnFind = QtWidgets.QPushButton("&Искать")
        self.btnFind.clicked.connect(self.findData)
        self.btnFind.setAutoDefault(True)
        self.btnFind.setDefault(True)
        hbox.addWidget(self.btnFind)
        vbox.addLayout(hbox)
        self.wvwMain = QtWebEngineWidgets.QWebEngineView()
        self.wvwMain.load(QtCore.QUrl(
            r'https://doc.qt.io/qt-6/index.html'))
        vbox.addWidget(self.wvwMain)
        self.setLayout(vbox)
        self.resize(600, 400)

    def findData(self):
        if self.chkWithCase.isChecked():
            self.wvwMain.findText(self.txtFind.text(),
            options=QtWebEngineCore.QWebEnginePage.FindFlag.FindCaseSensitively,
                                    resultCallback=showNumberOfMatches)
        else:
            self.wvwMain.findText(self.txtFind.text(),
                                  resultCallback=showNumberOfMatches)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
