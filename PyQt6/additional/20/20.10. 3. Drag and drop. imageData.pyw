from PyQt6 import QtCore, QtWidgets, QtGui

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                           QtWidgets.QFrame.Shadow.Plain)
        self.startPos = None

    def mousePressEvent(self, e):
        if e.buttons() & QtCore.Qt.MouseButton.LeftButton:
            self.startPos = e.pos()
        else:
            self.startPos = None
            e.ignore()
        QtWidgets.QLabel.mousePressEvent(self, e)

    def mouseMoveEvent(self, e):
        if self.startPos is None:
            e.ignore()
            QtWidgets.QLabel.mouseMoveEvent(self, e)
            return
        length = (e.pos() - self.startPos).manhattanLength()
        if length <= QtWidgets.QApplication.startDragDistance():
            e.ignore()
            QtWidgets.QLabel.mouseMoveEvent(self, e)
            return
        data = QtCore.QMimeData()
        data.setImageData(QtGui.QImage("pixmap.jpg"))
        drag = QtGui.QDrag(self)
        drag.setMimeData(data)
        drag.setPixmap(QtGui.QPixmap("pixmap.jpg"))
        drag.setHotSpot(QtCore.QPoint(1, 1))
        action = drag.exec(QtCore.Qt.DropAction.MoveAction |
                           QtCore.Qt.DropAction.CopyAction, 
                           QtCore.Qt.DropAction.MoveAction)
        if action == QtCore.Qt.DropAction.CopyAction:
            print("Завершено действие CopyAction")
        elif action == QtCore.Qt.DropAction.MoveAction:
            print("Завершено действие MoveAction")
        elif action == QtCore.Qt.DropAction.IgnoreAction:
            print("Действие отменено")
        QtWidgets.QLabel.mouseMoveEvent(self, e)

class MyLabel2(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                           QtWidgets.QFrame.Shadow.Plain)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasImage():
            e.acceptProposedAction()

    def dropEvent(self, e):
        if e.mimeData().hasImage():
            self.setPixmap(
                 QtGui.QPixmap.fromImage(e.mimeData().imageData()))
            e.accept()
        else:
            e.ignore()

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label1 = MyLabel("Щелкните здесь мышью\n" +
             "и перетащите на надпись ниже")
        self.label2 = MyLabel2("")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label1)
        self.vbox.addWidget(self.label2)
        self.setLayout(self.vbox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Перетаскивание и сброс изображения")
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())
