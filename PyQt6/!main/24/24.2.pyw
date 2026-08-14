from PyQt6 import QtWidgets, QtSql
import sys
app = QtWidgets.QApplication(sys.argv)
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()
# Проверяем, есть ли в базе данных таблица good, и, если таковой нет,
# создаем ее SQL-командой CREATE TABLE
if 'good' not in con.tables():
    query = QtSql.QSqlQuery()
    query.exec("create table good(id integer primary key autoincrement, " +
               "goodname text, goodcount integer) ")
con.close()
