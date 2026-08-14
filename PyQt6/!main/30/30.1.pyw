from PyQt6 import QtCore, QtWidgets, QtGui, QtPrintSupport
import sys
app = QtWidgets.QApplication(sys.argv)
# Создаем принтер
printer = QtPrintSupport.QPrinter()
# Для целей отладки лучше выводить документ не на принтер,
# а в файл в формате PDF. Чтобы сделать это, достаточно
# раскомментировать следующую строчку кода:
# printer.setOutputFileName("output.pdf")
# Создаем поверхность рисования и привязываем принтер к ней
painter = QtGui.QPainter()
painter.begin(printer)
# Рисуем рамку вокруг страницы
pen = QtGui.QPen(QtGui.QColor(QtCore.Qt.GlobalColor.blue), 5,
                              style=QtCore.Qt.PenStyle.DotLine)
painter.setPen(pen)
painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
page_size = printer.pageRect(QtPrintSupport.QPrinter.Unit.DevicePixel)
page_width = int(page_size.width())
page_height = int(page_size.height())
painter.drawRect(0, 0, page_width, page_height)
# Выводим надпись
color = QtGui.QColor(QtCore.Qt.GlobalColor.black)
painter.setPen(QtGui.QPen(color))
painter.setBrush(QtGui.QBrush(color))
font = QtGui.QFont("Verdana", pointSize=42)
painter.setFont(font)
painter.drawText(10, page_height // 2 - 100, page_width - 20,
                 50, QtCore.Qt.AlignmentFlag.AlignCenter |
                     QtCore.Qt.TextFlag.TextDontClip,
                 "QPrinter")
# Изменяем ориентацию страницы. Сделать это нужно перед вызовом
# метода newPage()
printer.setPageOrientation(QtGui.QPageLayout.Orientation.Landscape)
# Переходим на новую страницу
printer.newPage()
# Выводим изображение
page_size = printer.pageRect(QtPrintSupport.QPrinter.Unit.DevicePixel)
page_width = int(page_size.width())
page_height = int(page_size.height())
pixmap = QtGui.QPixmap("img.jpg")
pixmap = pixmap.scaled(page_width, page_height,
         aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
painter.drawPixmap(0, 0, pixmap)
painter.end()
