from PyQt6 import QtCore, QtWidgets, QtGui
import sys

def on_clicked():
    ind = view.currentIndex()
    if ind.isValid():
        print("Данные:", ind.data())
        print("Строка:", ind.row(), "Столбец:", ind.column())
    else:
        print("Нет текущего элемента")
    
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTableView")
window.resize(500, 200)
view = QtWidgets.QTableView()

model = QtGui.QStandardItemModel()
model.setRowCount(3)
model.setColumnCount(4)
for row in range(0, 3):
    for column in range(0, 4):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        model.setItem(row, column, item)

model.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, "A")
model.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, "B")
model.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, "C")
model.setHeaderData(3, QtCore.Qt.Orientation.Horizontal, "D")

model.setHeaderData(0, QtCore.Qt.Orientation.Vertical, "01")
model.setHeaderData(1, QtCore.Qt.Orientation.Vertical, "02")
model.setHeaderData(2, QtCore.Qt.Orientation.Vertical, "03")

print(model.headerData(0, QtCore.Qt.Orientation.Horizontal))

view.setModel(model)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
