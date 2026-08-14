from PyQt6 import QtWidgets, QtSql
import sys
app = QtWidgets.QApplication(sys.argv)
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()
query = QtSql.QSqlQuery()
query.exec("select * from good order by goodname")
lst = []
if query.isActive():
    query.first()
    while query.isValid():
        lst.append(query.value('goodname') + ': ' +
                   str(query.value('goodcount')) + ' шт.')
        query.next()
    for p in lst: print(p)
con.close()
