from PyQt6 import QtCore, QtWidgets, QtSql
import sys

def addRecord():
    # Вставляем пустую запись, в которую пользователь сможет
    # ввести нужные данные
    stm.insertRow(stm.rowCount())

def delRecord():
    # Удаляем запись из модели
    stm.removeRow(tv.currentIndex().row())
    # Выполняем повторное считывание данных в модель,
    # чтобы убрать пустую "мусорную" запись
    stm.select()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QSqlTableModel")
# Устанавливаем соединение с базой данных
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()
# Создаем модель
stm = QtSql.QSqlTableModel(parent=window)
stm.setTable('good')
stm.setSort(1, QtCore.Qt.SortOrder.AscendingOrder)
stm.select()
# Задаем заголовки для столбцов модели
stm.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, 'Название')
stm.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, 'Кол-во')
# Задаем для таблицы только что созданную модель
vbox = QtWidgets.QVBoxLayout()
tv = QtWidgets.QTableView()
tv.setModel(stm)
# Скрываем первый столбец, в котором выводится идентификатор
tv.hideColumn(0)
tv.setColumnWidth(1, 150)
tv.setColumnWidth(2, 60)
vbox.addWidget(tv)
btnAdd = QtWidgets.QPushButton("&Добавить запись")
btnAdd.clicked.connect(addRecord)
vbox.addWidget(btnAdd)
btnDel = QtWidgets.QPushButton("&Удалить запись")
btnDel.clicked.connect(delRecord)
vbox.addWidget(btnDel)
window.setLayout(vbox)
window.resize(370, 250)
window.show()
sys.exit(app.exec())
