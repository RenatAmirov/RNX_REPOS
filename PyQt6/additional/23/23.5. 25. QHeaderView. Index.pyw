from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    print("Логический: 0, Визуальный:", hHeader.visualIndex(0))
    print("Логический: 1, Визуальный:", hHeader.visualIndex(1))
    print("Логический: 2, Визуальный:", hHeader.visualIndex(2))
    print("Логический: 3, Визуальный:", hHeader.visualIndex(3))
    print("-" * 20)

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
hHeader.setSectionsMovable(True)

button = QtWidgets.QPushButton("Вывести значения")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
