from PyQt6 import QtCore, QtWidgets, QtWebEngineWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window)
        self.setWindowTitle("Класс QWebEngineView")
        vbox = QtWidgets.QVBoxLayout()
        self.wvwMain = QtWebEngineWidgets.QWebEngineView()
        self.wvwMain.setHtml("""
        <html>
          <head>
            <title>Ссылки</title>
          </head>
          <body>
            <p><a href='https://www.google.ru/'>Google</p>
            <p><a href='https://doc.qt.io/qt-6/index.html/'>Qt</p>
          </body>
        </html>
        """
        )
        self.wvwMain.setZoomFactor(3)
        vbox.addWidget(self.wvwMain)
        self.setLayout(vbox)
        self.resize(600, 400)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
