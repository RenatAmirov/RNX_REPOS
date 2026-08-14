from PyQt6 import QtCore, QtWidgets

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, prnt, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.grabMouse()
        self.prnt = prnt

    def mousePressEvent(self, e):
        l_pos = e.pos()
        g_pos = e.globalPosition()
        self.setText(
             "X: {0}, Y: {1}, Global X: {2}, Global Y: {3}".format(
             l_pos.x(), l_pos.y(), g_pos.x(), g_pos.y()))
        # Преобразование из глобальных координат в координаты компонента
        p1 = self.mapFromGlobal(g_pos)
        print("mapFromGlobal - X: {0}, Y: {1}".format(p1.x(), p1.y()))
        # Преобразование из координат компонента в глобальные координаты 
        p2 = self.mapToGlobal(l_pos)
        print("mapToGlobal - X: {0}, Y: {1}".format(p2.x(), p2.y()))
        # Преобразование в координаты родителя 
        p3 = self.mapToParent(l_pos)
        print("mapToParent - X: {0}, Y: {1}".format(p3.x(), p3.y()))
        # Преобразование координат родителя в координаты компонента 
        p4 = self.mapFromParent(p3)
        print("mapFromParent - X: {0}, Y: {1}".format(p4.x(), p4.y()))
        # Преобразование в координаты родителя 
        p5 = self.mapTo(self.prnt, l_pos)
        print("mapTo - X: {0}, Y: {1}".format(p5.x(), p5.y()))
        # Преобразование координат родителя в координаты компонента 
        p6 = self.mapFrom(self.prnt, p5)
        print("mapFrom - X: {0}, Y: {1}".format(p6.x(), p6.y()))
        e.ignore()
        QtWidgets.QLabel.mousePressEvent(self, e)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 150)
        self.label = MyLabel("Щелкните мышью в окне", self)
        self.label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                                 QtWidgets.QFrame.Shadow.Plain)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Пересчет координат курсора мыши")
    window.show()
    sys.exit(app.exec())
