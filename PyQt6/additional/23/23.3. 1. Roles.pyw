from PyQt6 import QtCore, QtWidgets, QtGui
import sys

def on_clicked():
    print("Текст:", comboBox.currentText())
    print("Данные:", comboBox.itemData(comboBox.currentIndex(), 
                                  role=QtCore.Qt.ItemDataRole.DisplayRole))
    print("Данные:", comboBox.itemData(0,
                                  role=QtCore.Qt.ItemDataRole.UserRole))
    print("Данные:", comboBox.itemData(0,
                                  role=QtCore.Qt.ItemDataRole.UserRole+1))
    
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QComboBox")
window.resize(300, 90)
comboBox = QtWidgets.QComboBox()
for i in range(1, 11):
    comboBox.addItem("Пункт {0}".format(i), i)
ico = window.style().standardIcon(
             QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical)
comboBox.setItemData(0, "Новое значение",
                     role=QtCore.Qt.ItemDataRole.DisplayRole)
comboBox.setItemData(0, ico, role=QtCore.Qt.ItemDataRole.DecorationRole)
comboBox.setItemData(0, QtGui.QFont("Courier New", 16), 
                     role=QtCore.Qt.ItemDataRole.FontRole)
comboBox.setItemData(1, QtCore.Qt.AlignmentFlag.AlignRight,
                     role=QtCore.Qt.ItemDataRole.TextAlignmentRole)
comboBox.setItemData(2, 
    QtGui.QBrush(QtGui.QColor("#000000"), QtCore.Qt.BrushStyle.SolidPattern),
    role=QtCore.Qt.ItemDataRole.BackgroundRole)
comboBox.setItemData(2, 
    QtGui.QBrush(QtGui.QColor("#FFFFFF"), QtCore.Qt.BrushStyle.SolidPattern),
    role=QtCore.Qt.ItemDataRole.ForegroundRole)
comboBox.setItemData(3, QtCore.Qt.CheckState.Checked,
                     role=QtCore.Qt.ItemDataRole.CheckStateRole)
comboBox.setItemData(4, QtCore.Qt.CheckState.PartiallyChecked,
                     role=QtCore.Qt.ItemDataRole.CheckStateRole)
comboBox.setItemData(5, QtCore.Qt.CheckState.Unchecked,
                     role=QtCore.Qt.ItemDataRole.CheckStateRole)
comboBox.setItemData(0, 50, role=QtCore.Qt.ItemDataRole.UserRole)
comboBox.setItemData(0, "Другие данные",
                     role=QtCore.Qt.ItemDataRole.UserRole+1)
comboBox.setItemData(0, "Это текст всплывающей подсказки",
                     role=QtCore.Qt.ItemDataRole.ToolTipRole)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
