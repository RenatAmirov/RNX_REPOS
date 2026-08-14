from PyQt6 import QtCore, QtWidgets

cursors = [
    (QtCore.Qt.CursorShape.ArrowCursor, "ArrowCursor"),
    (QtCore.Qt.CursorShape.UpArrowCursor, "UpArrowCursor"),
    (QtCore.Qt.CursorShape.CrossCursor, "CrossCursor"),
    (QtCore.Qt.CursorShape.WaitCursor, "WaitCursor"),
    (QtCore.Qt.CursorShape.IBeamCursor, "IBeamCursor"),
    (QtCore.Qt.CursorShape.SizeVerCursor, "SizeVerCursor"),
    (QtCore.Qt.CursorShape.SizeHorCursor, "SizeHorCursor"),
    (QtCore.Qt.CursorShape.SizeBDiagCursor, "SizeBDiagCursor"),
    (QtCore.Qt.CursorShape.SizeFDiagCursor, "SizeFDiagCursor"),
    (QtCore.Qt.CursorShape.SizeAllCursor, "SizeAllCursor"),
    (QtCore.Qt.CursorShape.SplitVCursor, "SplitVCursor"),
    (QtCore.Qt.CursorShape.SplitHCursor, "SplitHCursor"),
    (QtCore.Qt.CursorShape.PointingHandCursor, "PointingHandCursor"),
    (QtCore.Qt.CursorShape.ForbiddenCursor, "ForbiddenCursor"),
    (QtCore.Qt.CursorShape.OpenHandCursor, "OpenHandCursor"),
    (QtCore.Qt.CursorShape.ClosedHandCursor, "ClosedHandCursor"),
    (QtCore.Qt.CursorShape.WhatsThisCursor, "WhatsThisCursor"),
    (QtCore.Qt.CursorShape.BusyCursor, "BusyCursor")
]

class MyLabel(QtWidgets.QLabel):
    def __init__(self, cur, nameCur, parent=None):
        QtWidgets.QLabel.__init__(self, nameCur, parent)
        self.setFixedSize(150, 40)
        self.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                           QtWidgets.QFrame.Shadow.Plain)
        self.setCursor(cur)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.labels = []
        self.grid = QtWidgets.QGridLayout()
        i = 0
        for j in range(6):
            for k in range(3):
                item = MyLabel(cursors[i][0], cursors[i][1])
                self.labels.append(item)
                self.grid.addWidget(item, j, k)
                i += 1
        self.setLayout(self.grid)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Изменение курсора мыши")
    window.resize(500, 350)
    window.show()
    sys.exit(app.exec())
