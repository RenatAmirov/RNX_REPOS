from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QItemSelectionModel")
window.resize(300, 400)
tableView = QtWidgets.QTableView()
listView = QtWidgets.QListView()

model = QtGui.QStandardItemModel(3, 1)
for row in range(0, 3):
    item = QtGui.QStandardItem("Пункт {0}".format(row))
    model.setItem(row, 0, item)
model.setHorizontalHeaderLabels(["A"])
model.setVerticalHeaderLabels(["01", "02", "03"])

selModel = QtCore.QItemSelectionModel(model)

tableView.setModel(model)
listView.setModel(model)

tableView.setSelectionModel(selModel)
listView.setSelectionModel(selModel)

box = QtWidgets.QVBoxLayout()
box.addWidget(tableView)
box.addWidget(listView)
window.setLayout(box)
window.show()
sys.exit(app.exec())
