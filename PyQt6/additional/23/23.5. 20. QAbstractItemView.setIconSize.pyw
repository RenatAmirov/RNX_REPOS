from PyQt6 import QtCore, QtWidgets, QtGui
import sys

def on_clicked():
    for sel in view.selectedIndexes():
        print(sel.data())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QListView")
window.resize(300, 200)

view = QtWidgets.QListView()
view.setIconSize(QtCore.QSize(32, 32))

style = window.style()
icons = []
icons.append(style.standardIcon(
      QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical))
icons.append(style.standardIcon(
      QtWidgets.QStyle.StandardPixmap.SP_MessageBoxInformation))
icons.append(style.standardIcon(
      QtWidgets.QStyle.StandardPixmap.SP_MessageBoxWarning))
icons.append(style.standardIcon(
      QtWidgets.QStyle.StandardPixmap.SP_MessageBoxQuestion))
icons.append(style.standardIcon(
      QtWidgets.QStyle.StandardPixmap.SP_ComputerIcon))
icons.append(style.standardIcon(
      QtWidgets.QStyle.StandardPixmap.SP_DesktopIcon))

model = QtGui.QStandardItemModel(6, 1)
for row in range(0, 6):
    item = QtGui.QStandardItem(icons[row], "Пункт {0}".format(row))
    model.setItem(row, 0, item)
view.setModel(model)
view.setModelColumn(0)

button = QtWidgets.QPushButton("Вывести текст выделенных элементов")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
