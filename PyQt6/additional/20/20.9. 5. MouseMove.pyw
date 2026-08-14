from PyQt6 import QtCore, QtWidgets

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # Обрабатываем любые перемещения мыши
        self.setMouseTracking(True)
        # в пределах всего окна, а не комопонета
        self.grabMouse()

    def mouseMoveEvent(self, e):
        l_pos = e.pos()
        g_pos = e.globalPosition()
        self.setText(
             "X: {0}, Y: {1}, Global X: {2}, Global Y: {3}".format(
             l_pos.x(), l_pos.y(), g_pos.x(), g_pos.y()))
        e.ignore()
        QtWidgets.QLabel.mouseMoveEvent(self, e)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 150)
        self.label = MyLabel("Переместите мышь")
        self.label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                                 QtWidgets.QFrame.Shadow.Plain)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Перемещение курсора мыши")
    window.show()
    sys.exit(app.exec())
