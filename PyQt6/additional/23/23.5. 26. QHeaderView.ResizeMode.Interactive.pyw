from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    print(hHeader.defaultSectionSize())
    print(hHeader.minimumSectionSize())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTableView")
window.resize(500, 400)
view = QtWidgets.QTableView()

model = QtGui.QStandardItemModel(3, 4)
for row in range(0, 3):
    for column in range(0, 4):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        model.setItem(row, column, item)
model.setHorizontalHeaderLabels(["A", "B", "C", "D"])
model.setVerticalHeaderLabels(["01", "02", "03"])
view.setModel(model)

hHeader = view.horizontalHeader()
hHeader.setDefaultSectionSize(100)
hHeader.setMinimumSectionSize(50)
hHeader.resizeSection(3, 200)
hHeader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Interactive)

button = QtWidgets.QPushButton("Вывести значения")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
