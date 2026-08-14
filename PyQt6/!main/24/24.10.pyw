from PyQt6 import QtCore, QtWidgets, QtSql
import sys

def addRecord():
    stm.insertRow(stm.rowCount())

def delRecord():
    stm.removeRow(tv.currentIndex().row())
    stm.select()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QRelationalSqlTableModel")
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()
stm = QtSql.QSqlRelationalTableModel(parent=window)
stm.setTable('good')
stm.setSort(1, QtCore.Qt.SortOrder.AscendingOrder)
# Задаем для поля категории связь с таблицей списка категорий
stm.setRelation(3, QtSql.QSqlRelation('category', 'id', 'catname'))
stm.select()
stm.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, 'Название')
stm.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, 'Кол-во')
stm.setHeaderData(3, QtCore.Qt.Orientation.Horizontal, 'Категория')
vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)
tv.hideColumn(0)
tv.setColumnWidth(1, 150)
tv.setColumnWidth(2, 60)
tv.setColumnWidth(3, 150)
vbox.addWidget(tv)
btnAdd = QtWidgets.QPushButton("&Добавить запись")
btnAdd.clicked.connect(addRecord)
vbox.addWidget(btnAdd)
btnDel = QtWidgets.QPushButton("&Удалить запись")
btnDel.clicked.connect(delRecord)
vbox.addWidget(btnDel)
window.setLayout(vbox)
window.resize(420, 250)
window.show()
sys.exit(app.exec())
