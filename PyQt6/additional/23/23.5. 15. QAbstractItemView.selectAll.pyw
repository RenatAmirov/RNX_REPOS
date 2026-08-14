from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    view.setFocus()
    view.clearSelection()

def on_clicked2():
    view.setFocus()
    view.selectAll()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QListView")
window.resize(300, 200)

view = QtWidgets.QListView()
view.setSelectionMode(
        QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)

L = []
for i in range(1, 101):
    L.append("Пункт {0}".format(i))
model = QtCore.QStringListModel(L)
view.setModel(model)

button = QtWidgets.QPushButton("Снять выделение")
button.clicked.connect(on_clicked)
button2 = QtWidgets.QPushButton("Выделить все")
button2.clicked.connect(on_clicked2)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
box.addWidget(button2)
window.setLayout(box)
window.show()
sys.exit(app.exec())
