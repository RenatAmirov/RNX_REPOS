from PyQt6 import QtCore, QtWidgets, QtGui
import sys

def on_clicked():
    s = line.text()
    proxyModel.setFilterRegularExpression(s)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QSortFilterProxyModel")
window.resize(600, 500)
view1 = QtWidgets.QTableView()
view2 = QtWidgets.QTableView()

view1.setSortingEnabled(True)

model = QtGui.QStandardItemModel(6, 4)
for row in range(0, 4):
    for column in range(0, 4):
        item = QtGui.QStandardItem(
            "Пункт ({0}, {1})".format(row, column))
        model.setItem(row, column, item)
for row in range(4, 6):
    for column in range(0, 4):
        item = QtGui.QStandardItem(
            "Новый элемент ({0}, {1})".format(row, column))
        model.setItem(row, column, item)

proxyModel = QtCore.QSortFilterProxyModel()
proxyModel.setFilterKeyColumn(-1)
proxyModel.setFilterRegularExpression("[0-2], [0-9]")
proxyModel.setSourceModel(model)

view1.setModel(proxyModel)
view2.setModel(model)

line = QtWidgets.QLineEdit()
button = QtWidgets.QPushButton("Отфильтровать")
button.clicked.connect(on_clicked)

hbox = QtWidgets.QHBoxLayout()
hbox.addWidget(line)
hbox.addWidget(button)

box = QtWidgets.QVBoxLayout()
box.addWidget(QtWidgets.QLabel("Промежуточная модель"))
box.addWidget(view1)
box.addLayout(hbox)
box.addWidget(QtWidgets.QLabel("Базовая модель"))
box.addWidget(view2)
window.setLayout(box)
window.show()
sys.exit(app.exec())
