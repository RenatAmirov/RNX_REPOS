from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    ind = listView.currentIndex()
    if ind.isValid():
        print("Данные:", ind.data())
        print("Строка:", ind.row())
    else:
        print("Нет текущего элемента")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QListView")
window.resize(300, 200)
listView = QtWidgets.QListView()
L = []
for i in range(1, 11):
    L.append("Пункт {0}".format(i))
model = QtCore.QStringListModel(L)
listView.setModel(model)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(listView)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
