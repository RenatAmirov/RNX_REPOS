from PyQt6 import QtCore, QtWidgets

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.grabMouse()

    def wheelEvent(self, e):
        if e.angleDelta().y() > 0:
            print("Колесико повернуто от пользователя")
        elif e.angleDelta().y() < 0:
            print("Колесико повернуто к пользователю")
        if e.buttons() & QtCore.Qt.MouseButton.LeftButton:
            print("Нажата левая кнопка мыши")
        if e.buttons() & QtCore.Qt.MouseButton.RightButton:
            print("Нажата правая кнопка мыши")
        if e.buttons() & QtCore.Qt.MouseButton.MiddleButton:
            print("Нажата средняя кнопка мыши")
        if (e.buttons() & QtCore.Qt.MouseButton.LeftButton and 
            e.buttons() & QtCore.Qt.MouseButton.RightButton):
            print("Левая и правая кнопки нажаты")
        l_pos = e.position()
        g_pos = e.globalPosition()
        self.setText(
          "X: {0}, Y: {1}, Global X: {2}, Global Y: {3}\ndelta: {4}".format(
          l_pos.x(), l_pos.y(), g_pos.x(), g_pos.y(), e.angleDelta().y()))
        e.ignore()
        QtWidgets.QLabel.wheelEvent(self, e)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 150)
        self.label = MyLabel("Поверните колесико мыши")
        self.label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                                 QtWidgets.QFrame.Shadow.Plain)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Вращение колесика мыши")
    window.show()
    sys.exit(app.exec())
