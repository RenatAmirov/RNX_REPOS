from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    view.setModel(model)
    button.setEnabled(False)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QListView")
window.resize(300, 150)
view = QtWidgets.QListView()

view.setLayoutMode(QtWidgets.QListView.LayoutMode.Batched)
view.setBatchSize(100)

L = []
for i in range(1, 100000):
    L.append("Пункт {0}".format(i))
model = QtCore.QStringListModel(L)

L2 = []
for i in range(1, 5):
    L2.append("Пункт {0}".format(i))
model2 = QtCore.QStringListModel(L2)
view.setModel(model2)

button = QtWidgets.QPushButton("Установить модель")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
