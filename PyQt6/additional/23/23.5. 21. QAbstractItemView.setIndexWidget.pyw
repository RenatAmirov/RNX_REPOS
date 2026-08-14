from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    print("Нажата кнопка")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTableView")
window.resize(500, 200)

view = QtWidgets.QTableView()

model = QtGui.QStandardItemModel(4, 4)
for row in range(0, 4):
    for column in range(0, 4):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        model.setItem(row, column, item)
view.setModel(model)

button = QtWidgets.QPushButton("Кнопка")
view.setIndexWidget(model.index(0, 0), button)
b = view.indexWidget(model.index(0, 0))
b.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)
window.show()
sys.exit(app.exec())
