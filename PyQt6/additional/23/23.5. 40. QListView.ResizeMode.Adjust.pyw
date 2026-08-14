from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    ind = view.currentIndex()
    if ind.isValid():
        print("Данные:", ind.data())
        print("Строка:", ind.row())
    else:
        print("Нет текущего элемента")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QListView")
window.resize(300, 200)
view = QtWidgets.QListView()
view.setViewMode(QtWidgets.QListView.ViewMode.IconMode)
view.setResizeMode(QtWidgets.QListView.ResizeMode.Adjust)

style = window.style()
icons = []
icons.append(style.standardIcon(
      QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical))
icons.append(style.standardIcon(
      QtWidgets.QStyle.StandardPixmap.SP_MessageBoxInformation))
icons.append(style.standardIcon(
      QtWidgets.QStyle.StandardPixmap.SP_MessageBoxWarning))
icons.append(style.standardIcon(
      QtWidgets.QStyle.StandardPixmap.SP_MessageBoxQuestion))
icons.append(style.standardIcon(
      QtWidgets.QStyle.StandardPixmap.SP_ComputerIcon))
icons.append(style.standardIcon(
      QtWidgets.QStyle.StandardPixmap.SP_DesktopIcon))

model = QtGui.QStandardItemModel(6, 1)
for row in range(0, 6):
    item = QtGui.QStandardItem(icons[row], "Пункт {0}".format(row))
    model.setItem(row, 0, item)
view.setModel(model)
view.setModelColumn(0)

button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
