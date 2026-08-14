from PyQt6 import QtGui, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QStandardItemModel")
tv = QtWidgets.QTableView(parent=window)
sti = QtGui.QStandardItemModel(parent=window)
lst1 = ['Perl', 'PHP', 'Python', 'Ruby']
lst2 = ['http://www.perl.org/', 'http://php.net/', 'https://www.python.org/',
        'https://www.ruby-lang.org/']
for row in range(0, 4):
    if row == 2:
        iconfile = 'python.png'
    else:
        iconfile = 'icon.png'
    item1 = QtGui.QStandardItem(QtGui.QIcon(iconfile), '')
    item2 = QtGui.QStandardItem(lst1[row])
    item3 = QtGui.QStandardItem(lst2[row])
    sti.appendRow([item1, item2, item3])
sti.setHorizontalHeaderLabels(['Значок', 'Название', 'Сайт'])
tv.setModel(sti)
tv.setColumnWidth(0, 50)
tv.setColumnWidth(2, 180)
tv.resize(350, 150)
window.show()
sys.exit(app.exec())
