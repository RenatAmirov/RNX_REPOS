from PyQt6 import QtWidgets, QtSql
import sys
app = QtWidgets.QApplication(sys.argv)
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()
query = QtSql.QSqlQuery()
query.prepare("insert into good values(null, :name, :count)")
lst1 = ['Бумага офисная', 'Фотобумага', 'Картридж']
lst2 = [15, 8, 3]
query.bindValue(':name', lst1)
query.bindValue(':count', lst2)
query.execBatch()
con.close()
