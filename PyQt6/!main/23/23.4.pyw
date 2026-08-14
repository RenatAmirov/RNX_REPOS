from PyQt6 import QtCore, QtWidgets, QtGui
import sys

# Создаем класс делегата
class SpinBoxDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, options, index):
        # Создаем компонент-редактор, используемый для правки значений
        # количества позиций
        editor = QtWidgets.QSpinBox(parent)
        editor.setFrame(False)
        editor.setMinimum(0)
        editor.setSingleStep(1)
        return editor
    def setEditorData(self, editor, index):
        # Заносим в компонент-редактор значение количества
        value = int(index.model().data(index, QtCore.Qt.ItemDataRole.EditRole))
        editor.setValue(value)
    def updateEditorGeometry(self, editor, options, index):
        # Указываем размеры компонента-редактора
        editor.setGeometry(options.rect)
    def setModelData(self, editor, model, index):
        # Заносим исправленное значение количества в модель
        value = str(editor.value())
        model.setData(index, value, QtCore.Qt.ItemDataRole.EditRole);

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QTableView()
window.setWindowTitle("Использование делегата")
sti = QtGui.QStandardItemModel(parent=window)
lst1 = ['Флэш-диск', 'Бумага для принтера', 'Картридж для принтера']
lst2 = ["10", "3", "8"]
for row in range(0, 3):
    item1 = QtGui.QStandardItem(lst1[row])
    item2 = QtGui.QStandardItem(lst2[row])
    sti.appendRow([item1, item2])
sti.setHorizontalHeaderLabels(['Товар', 'Кол-во'])
window.setModel(sti)
# Назначаем делегат второму столбцу таблицы
window.setItemDelegateForColumn(1, SpinBoxDelegate())
window.setColumnWidth(0, 150)
window.resize(350, 150)
window.show()
sys.exit(app.exec())
