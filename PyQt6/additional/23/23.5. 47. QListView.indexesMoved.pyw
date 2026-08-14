from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    for sel in view.selectedIndexes():
        print(sel.data())

def on_indexes_moved(arr):
    for sel in arr:
        print(sel.data())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QListView")
window.resize(300, 200)

view = QtWidgets.QListView()
view.setViewMode(QtWidgets.QListView.ViewMode.IconMode)
view.setSelectionMode(
        QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
view.setMovement(QtWidgets.QListView.Movement.Free)

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

view.indexesMoved["const QModelIndexList&"].connect(on_indexes_moved)
button = QtWidgets.QPushButton("Получить текст выделенных элементов")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
