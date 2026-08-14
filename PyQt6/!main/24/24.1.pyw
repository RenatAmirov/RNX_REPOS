from PyQt6 import QtWidgets, QtSql
import sys
# Создаем объект программы, иначе поддержка баз данных не будет работать
app = QtWidgets.QApplication(sys.argv)

# Открываем базу данных SQLite, находящуюся в том же каталоге, что и файл
# с этой программой
con1 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con1.setDatabaseName('data.sqlite')
con1.open()
con1.close()

# Открываем базу данных MySQL
con2 = QtSql.QSqlDatabase.addDatabase('QMYSQL')
con2.setHostName("somehost");
con2.setDatabaseName("somedb");
con2.setUserName("someuser");
con2.setPassword("password");
con2.open();
con2.close()

# Открываем базу данных Microsoft Access через ODBC
con3 = QtSql.QSqlDatabase.addDatabase("QODBC");
con3.setDatabaseName("DRIVER={Microsoft Access Driver (*.mdb)};" +
                     "FIL={MS Access};DBQ=c:/book/data.mdb");
con3.open()
con3.close()
