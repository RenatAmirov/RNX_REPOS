from PyQt6 import QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QListView")
window.resize(600, 200)

view = QtWidgets.QListView()
view.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.InternalMove)
L = []
for i in range(1, 11):
    L.append("Пункт {0}".format(i))
model = QtCore.QStringListModel(L)
view.setModel(model)

view2 = QtWidgets.QListView()
view2.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DropOnly)
model2 = QtCore.QStringListModel([])
view2.setModel(model2)

box = QtWidgets.QHBoxLayout()
box.addWidget(view)
box.addWidget(view2)
window.setLayout(box)
window.show()
sys.exit(app.exec())
