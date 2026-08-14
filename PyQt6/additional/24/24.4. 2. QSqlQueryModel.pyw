from PyQt6 import QtCore, QtWidgets, QtGui, QtSql
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window)
        self.setWindowTitle("Фильтрация и сортировка данных")
        con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName('data3.sqlite')
        con.open()
        self.model = QtSql.QSqlQueryModel(parent=self)
        self.model.setQuery('select * from good order by goodname')
        self.model.setHeaderData(1, QtCore.Qt.Orientation.Horizontal,
                                 'Название')
        self.model.setHeaderData(2, QtCore.Qt.Orientation.Horizontal,
                                 'Кол-во')
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        lblSort = QtWidgets.QLabel("&Сортировка по полю")
        hbox.addWidget(lblSort)
        self.cboSort = QtWidgets.QComboBox()
        good_table = con.record("good")
        field_count = good_table.count()
        for field in range(0, field_count):
            field_name = good_table.field(field).name()
            if field_name != "id":
                self.cboSort.addItem(field_name)
        lblSort.setBuddy(self.cboSort)
        hbox.addWidget(self.cboSort)
        self.chkDesc = QtWidgets.QCheckBox("По &убыванию")
        hbox.addWidget(self.chkDesc,
                       alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        vbox.addLayout(hbox)
        hbox = QtWidgets.QHBoxLayout()
        lblFilterName = QtWidgets.QLabel("Фильтрация по &названию")
        hbox.addWidget(lblFilterName)
        self.txtFilterName = QtWidgets.QLineEdit()
        lblFilterName.setBuddy(self.txtFilterName)
        hbox.addWidget(self.txtFilterName)
        vbox.addLayout(hbox)
        hbox = QtWidgets.QHBoxLayout()
        lblFilterCount = QtWidgets.QLabel("Фильтрация по &кол-ву от")
        hbox.addWidget(lblFilterCount)
        self.spnFilterCount = QtWidgets.QSpinBox()
        lblFilterCount.setBuddy(self.spnFilterCount)
        hbox.addWidget(self.spnFilterCount)
        lblFilterCount2 = QtWidgets.QLabel("&до")
        hbox.addWidget(lblFilterCount2,
                       alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        self.spnFilterCount2 = QtWidgets.QSpinBox()
        lblFilterCount2.setBuddy(self.spnFilterCount2)
        hbox.addWidget(self.spnFilterCount2)
        vbox.addLayout(hbox)
        btnRefresh = QtWidgets.QPushButton("&Обновить")
        btnRefresh.clicked.connect(self._refreshData)
        vbox.addWidget(btnRefresh)
        self.tblMain = QtWidgets.QTableView()
        self.tblMain.setModel(self.model)
        self.tblMain.hideColumn(0)
        self.tblMain.setColumnWidth(1, 150)
        self.tblMain.setColumnWidth(2, 60)
        vbox.addWidget(self.tblMain)
        self.setLayout(vbox)
        self.resize(350, 350)

    def _refreshData(self):
        s = ""
        name = self.txtFilterName.text()
        count = self.spnFilterCount.value()
        count2 = self.spnFilterCount2.value()
        if name:
            s += "where goodname like '%" + name + "%'"
        if count or count2:
            if s:
                s += " and "
            else:
                s += "where "
            if count and not count2:
                s += "goodcount >= " + str(count)
            elif not count and count2:
                s += "goodcount <= " + str(count2)
            elif count and count2:
                if count == count2:
                    s += "goodcount = " + str(count)
                else:
                    s += "goodcount between " + str(count) + " and " + \
                         str(count2)
        s += " order by " + self.cboSort.currentText()
        if self.chkDesc.isChecked():
            s += " desc"
        self.model.setQuery("select * from good " + s)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
