from PyQt6 import QtWidgets, QtSql
import sys
app = QtWidgets.QApplication(sys.argv)
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()
query = QtSql.QSqlQuery()
query.prepare("insert into good values(null, ?, ?)")
query.bindValue(0, 'Компакт-диск')
query.bindValue(1, 5)
query.exec()
con.close()
