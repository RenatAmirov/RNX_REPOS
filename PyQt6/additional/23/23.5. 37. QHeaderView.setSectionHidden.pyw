from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    hHeader.setSectionHidden(0, False)

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
hHeader.setSectionHidden(0, True)

button = QtWidgets.QPushButton("Отобразить секцию 1")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
