from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    for sel in view.selectedIndexes():
        print(sel.data())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QListView")
window.resize(300, 200)

view = QtWidgets.QListView()
view.setAutoScroll(True)
view.setAutoScrollMargin(30)

view.setMovement(QtWidgets.QListView.Movement.Free)
view.setDragEnabled(True)

L = []
for i in range(1, 101):
    L.append("Пункт {0}".format(i))
model = QtCore.QStringListModel(L)
view.setModel(model)

button = QtWidgets.QPushButton("Вывести текст выделенных элементов")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
