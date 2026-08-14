from PyQt6 import QtCore, QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QSortFilterProxyModel")
window.resize(600, 500)
view1 = QtWidgets.QTableView()
view2 = QtWidgets.QTableView()
view1.setSortingEnabled(True)

model = QtGui.QStandardItemModel(4, 4)
for row in range(0, 4):
    for column in range(0, 4):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        model.setItem(row, column, item)

proxyModel = QtCore.QSortFilterProxyModel()
proxyModel.setSourceModel(model)

view1.setModel(proxyModel)
view2.setModel(model)

box = QtWidgets.QVBoxLayout()
box.addWidget(view1)
box.addWidget(view2)
window.setLayout(box)
window.show()
sys.exit(app.exec())
