from PyQt6 import QtWidgets, QtGui
import sys

def on_section_pressed(ind):
    print("on_section_pressed", ind)

def on_section_clicked(ind):
    print("on_section_clicked", ind)

def on_section_double_clicked(ind):
    print("on_section_double_clicked", ind)

def on_section_moved(ind, old, new):
    print("on_section_moved", ind, old, new)

def on_section_resized(ind, old, new):
    print("on_section_resized", ind, old, new)

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

hHeader.sectionPressed[int].connect(on_section_pressed)
hHeader.sectionClicked[int].connect(on_section_clicked)
hHeader.sectionDoubleClicked[int].connect(on_section_double_clicked)
hHeader.sectionMoved[int, int, int].connect(on_section_moved)
hHeader.sectionResized[int, int, int].connect(on_section_resized)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
window.setLayout(box)
window.show()
sys.exit(app.exec())
