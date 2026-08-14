from PyQt6 import QtWidgets, QtGui
import sys

state = None

def on_clicked():
    global state
    state = hHeader.saveState()
    
def on_clicked2():
    if state is not None:
        hHeader.restoreState(state)

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

button = QtWidgets.QPushButton("Сохранить")
button.clicked.connect(on_clicked)
button2 = QtWidgets.QPushButton("Восстановить")
button2.clicked.connect(on_clicked2)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
box.addWidget(button2)
window.setLayout(box)
window.show()
sys.exit(app.exec())
