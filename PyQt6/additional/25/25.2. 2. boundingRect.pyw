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
        
        painter.setPen(QtGui.QPen(red, 1))
        painter.setFont(QtGui.QFont("Tahoma", 12))
        
        painter.drawRect(QtCore.QRect(20, 40, 260, 200))
        textOption = QtGui.QTextOption(QtCore.Qt.AlignmentFlag.AlignCenter)
        textOption.setFlags(QtGui.QTextOption.Flag.ShowTabsAndSpaces)
        painter.drawText(QtCore.QRectF(20., 40., 260., 200.), 
                         "Показаны все\tспециальные символы ",
                         option=textOption)

        print(painter.boundingRect(20, 100, 260, 30, 
              QtCore.Qt.AlignmentFlag.AlignCenter |
              QtCore.Qt.TextFlag.TextShowMnemonic,
              "Строка &1"))
        
        print(painter.boundingRect(QtCore.QRect(20, 140, 260, 50), 
              QtCore.Qt.AlignmentFlag.AlignRight |
              QtCore.Qt.TextFlag.TextSingleLine,
              "Строка 2\nвсе специальные символы трактуются как пробелы и текст выводится в одну строку"))
        
        print(painter.boundingRect(QtCore.QRectF(20., 190., 260., 50.), 
              QtCore.Qt.AlignmentFlag.AlignRight |
              QtCore.Qt.TextFlag.TextWordWrap,
              "Строка 3 очень длинный текст на двух строках"))
        
        print(painter.boundingRect(QtCore.QRectF(20., 40., 260., 200.), 
              "Показаны все\tспециальные символы ",
              option=textOption))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Класс QPainter")
    window.show()
    sys.exit(app.exec())
