from PyQt6 import QtCore, QtWidgets, QtGui, QtSql
import os, sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window)
        self.setWindowTitle("Вывод сведений о базе данных")
        vbox = QtWidgets.QVBoxLayout()
        btnOpen = QtWidgets.QPushButton("&Открыть файл...")
        btnOpen.clicked.connect(self._openFile)
        vbox.addWidget(btnOpen)
        self.setLayout(vbox)
        self.txtOutput = QtWidgets.QTextEdit()
        self.txtOutput.setReadOnly(True)
        self.txtOutput.setWordWrapMode(QtGui.QTextOption.WrapMode.NoWrap)
        self.txtOutput.setFontFamily("Courier")
        vbox.addWidget(self.txtOutput)
        self.resize(400, 300)

    def _openFile(self):
        file, f = QtWidgets.QFileDialog.getOpenFileName(parent=self,
                    caption="Выберите файл базы данных",
                    filter="Базы данных SQLite (*.sqlite *.sqlite3)")
        if f:
            self._showParameters(file)

    def _showParameters(self, file):
        s = "База данных: " + os.path.basename(file) + "\n"
        s += "Путь: " + file + "\n\n"
        con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName(file)
        con.open()
        if con.isOpen():
            tables = con.tables()
            table_count = len(tables)
            s += "Всего таблиц: " + str(table_count) +  "\n\n"
            if table_count > 0:
                s += "Таблицы...\n"
                for t in tables:
                    s += "  " + t + ":\n"
                    table = con.record(t)
                    field_count = table.count()
                    for field_index in range(0, field_count):
                        field = table.field(field_index)
                        s2 = "    " + field.name() + ": "
                        match field.metaType().id():
                            case 1:
                                s2 += "bool"
                            case 2 | 4 | 32:
                                s2 += "int"
                            case 6 | 38:
                                s2 += "float"
                            case 10:
                                s2 += "str"
                            case 14:
                                s2 += "date"
                            case 15:
                                s2 += "time"
                            case 16:
                                s2 += "datetime"
                            case 3 | 5 | 35:
                                s2 += "unsigned int"
                            case 12:
                                s2 += "bytes"
                            case 0:
                                s2 += "unknown"
                        if (n := field.length()) > 0:
                            s2 += ", length: " + str(n)
                        if (n := field.precision()) > 0:
                            s2 += ", precision: " + str(n)
                        if (n := field.defaultValue()):
                            s2 += ", default: " + str(n)
                        if field.requiredStatus() == \
                           QtSql.QSqlField.RequiredStatus.Required:
                            s2 += ", required"
                        if field.isAutoValue():
                            s2 += ", autoincrement"
                        if field.isReadOnly():
                            s2 += ", readonly"
                        s += s2 + "\n"
                    s += "\n"
        else:
            s += "Возникла ошибка: " + con.lastError().text()
        con.close()
        self.txtOutput.setText(s)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
