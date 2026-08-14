from PyQt6 import QtCore, QtWidgets

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # Запрет передачи события родителю
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_NoMousePropagation,
                          True)

    def mousePressEvent(self, e):
        if e.buttons() & QtCore.Qt.MouseButton.LeftButton:
            print("Нажата левая кнопка мыши")
        if e.buttons() & QtCore.Qt.MouseButton.RightButton:
            print("Нажата правая кнопка мыши")
        if e.buttons() & QtCore.Qt.MouseButton.MiddleButton:
            print("Нажата средняя кнопка мыши")
        if (e.buttons() & QtCore.Qt.MouseButton.LeftButton and 
            e.buttons() & QtCore.Qt.MouseButton.RightButton):
            print("Левая и правая кнопки нажаты")
        l_pos = e.pos()
        g_pos = e.globalPosition()
        self.setText(
             "X: {0}, Y: {1}, Global X: {2}, Global Y: {3}".format(
             l_pos.x(), l_pos.y(), g_pos.x(), g_pos.y()))
        e.ignore()
        QtWidgets.QLabel.mousePressEvent(self, e)

    def mouseReleaseEvent(self, e):
        print("Отпускание кнопки")
        QtWidgets.QLabel.mouseReleaseEvent(self, e)

    def mouseDoubleClickEvent(self, e):
        print("Двойной щелчок")
        QtWidgets.QLabel.mouseDoubleClickEvent(self, e)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent) 
        self.resize(300, 150)
        self.label = MyLabel("Щелкните здесь мышью")
        self.label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                                 QtWidgets.QFrame.Shadow.Plain)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Нажатие и отпускание кнопок мыши")
    window.show()
    sys.exit(app.exec())
