from PyQt6 import QtWidgets
import sys
import PrintList
app = QtWidgets.QApplication(sys.argv)
pl = PrintList.PrintList()
# Если требуется вывести документ в файл формата PDF,
# следует раскомментировать эту строку:
# pl.printer.setOutputFileName("output.pdf")
data = []
for b in range(1, 101):
    data.append([b, b ** 2, b ** 3])
pl.data = data
pl.columnWidths = [100, 100, 200]
pl.headers = ["Аргумент", "Квадрат", "Куб"]
pl.printData()
