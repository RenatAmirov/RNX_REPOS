from PyQt6 import QtCore, QtWidgets

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def enterEvent(self, e):
        self.setText("Указатель в области компонента")
        QtWidgets.QLabel.enterEvent(self, e)

    def leaveEvent(self, e):
        self.setText("Указатель вне области компонента")
        QtWidgets.QLabel.leaveEvent(self, e)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 150)
        self.label = MyLabel("Наведите мышь на рамку")
        self.label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                                 QtWidgets.QFrame.Shadow.Plain)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Наведение и увод курсора мыши")
    window.show()
    sys.exit(app.exec())
