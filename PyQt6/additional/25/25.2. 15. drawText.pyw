from PyQt6 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 300)
    
    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        black = QtCore.Qt.GlobalColor.black
        white = QtCore.Qt.GlobalColor.white
        red = QtCore.Qt.GlobalColor.red
        painter.setPen(QtGui.QPen(black))
        painter.setBrush(QtGui.QBrush(white))
        painter.drawRect(3, 3, 294, 294)

        painter.setRenderHint(QtGui.QPainter.RenderHint.TextAntialiasing)
        painter.setPen(QtGui.QPen(red, 1))
        painter.setFont(QtGui.QFont("Tahoma", 12))
        painter.drawText(20, 30, "Строка 1")
        painter.drawText(QtCore.QPoint(150, 30), "Строка 2")
        
        painter.drawRect(QtCore.QRect(20, 40, 210, 50))
        print(painter.drawText(20, 40, 210, 50, 
              QtCore.Qt.TextFlag.TextDontClip,
              "Строка 3 текст будет выходить за границы"))
        
        painter.drawRect(QtCore.QRect(20, 100, 260, 30))
        print(painter.drawText(20, 100, 260, 30, 
              QtCore.Qt.AlignmentFlag.AlignCenter |
              QtCore.Qt.TextFlag.TextShowMnemonic,
              "Строка &4"))
        
        painter.drawRect(QtCore.QRect(20, 140, 260, 50))
        print(painter.drawText(QtCore.QRect(20, 140, 260, 50), 
              QtCore.Qt.AlignmentFlag.AlignRight |
              QtCore.Qt.TextFlag.TextSingleLine,
              "Строка 5\nвсе специальные символы трактуются как пробелы и текст выводится в одну строку"))
        
        painter.drawRect(QtCore.QRect(20, 190, 260, 50))
        print(painter.drawText(QtCore.QRect(20, 190, 260, 50), 
              QtCore.Qt.AlignmentFlag.AlignRight |
              QtCore.Qt.TextFlag.TextWordWrap,
              "Строка 6 очень длинный текст на двух строках"))
        
        painter.drawRect(QtCore.QRect(20, 240, 260, 50))
        print(painter.drawText(QtCore.QRect(20, 240, 260, 50), 
              QtCore.Qt.AlignmentFlag.AlignRight |
              QtCore.Qt.TextFlag.TextWrapAnywhere,
              "Строка7оченьдлинныйтекстнадвухстроках"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPainter")
    window.show()
    sys.exit(app.exec())
