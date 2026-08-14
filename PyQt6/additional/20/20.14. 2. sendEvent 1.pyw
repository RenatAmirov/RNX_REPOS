from PyQt6 import QtCore, QtWidgets, QtGui

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                           QtWidgets.QFrame.Shadow.Plain)

    def mousePressEvent(self, e):
        if e.buttons() & QtCore.Qt.MouseButton.LeftButton:
            print("Нажата левая кнопка мыши")
        p = e.pos()
        self.setText("X: {0}, Y: {1}".format(p.x(), p.y()))
        e.ignore()
        QtWidgets.QLabel.mousePressEvent(self, e)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = MyLabel("")
        self.button = QtWidgets.QPushButton("Отправить сообщение")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        e = QtGui.QMouseEvent(QtCore.QEvent.Type.MouseButtonPress,
                   QtCore.QPointF(5, 5), QtCore.Qt.MouseButton.LeftButton,
                   QtCore.Qt.MouseButton.LeftButton,
                   QtCore.Qt.KeyboardModifier.NoModifier)
        QtWidgets.QApplication.sendEvent(self.label, e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) 
    window = MyWindow()
    window.setWindowTitle("sendEvent")
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec())
