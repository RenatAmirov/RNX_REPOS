from PyQt6 import QtCore, QtWidgets, QtSql
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QTableView()
window.setWindowTitle("QSqlQueryModel")
# Устанавливаем соединение с базой данных
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()
# Создаем модель
sqm = QtSql.QSqlQueryModel(parent=window)
sqm.setQuery('select * from good order by goodname')
# Задаем заголовки для столбцов модели
sqm.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, 'Название')
sqm.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, 'Кол-во')
# Задаем для таблицы только что созданную модель
window.setModel(sqm)
# Скрываем первый столбец, в котором выводится идентификатор
window.hideColumn(0)
window.setColumnWidth(1, 150)
window.setColumnWidth(2, 60)
window.resize(260, 160)
window.show()
sys.exit(app.exec())
