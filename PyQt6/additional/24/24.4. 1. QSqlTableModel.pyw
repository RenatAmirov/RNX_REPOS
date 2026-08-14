from PyQt6 import QtCore, QtWidgets, QtGui, QtSql
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window)
        self.setWindowTitle("Работа с данными")
        con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        con.setDatabaseName('data3.sqlite')
        con.open()
        self.model = QtSql.QSqlTableModel(parent=self)
        self.model.setTable('good')
        self.model.setSort(1, QtCore.Qt.SortOrder.AscendingOrder)
        self.model.select()
        self.model.setHeaderData(1,
                                 QtCore.Qt.Orientation.Horizontal, 'Название')
        self.model.setHeaderData(2,
                                 QtCore.Qt.Orientation.Horizontal, 'Кол-во')
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
        hbox = QtWidgets.QHBoxLayout()
        self.btnAdd = QtWidgets.QPushButton("&Добавить запись")
        self.btnAdd.clicked.connect(self._addRecord)
        hbox.addWidget(self.btnAdd)
        self.btnDel = QtWidgets.QPushButton("&Удалить запись")
        self.btnDel.clicked.connect(self._delRecord)
        hbox.addWidget(self.btnDel)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.resize(300, 400)

    def _refreshData(self):
        s = ""
        name = self.txtFilterName.text()
        count = self.spnFilterCount.value()
        count2 = self.spnFilterCount2.value()
        if name:
            s += "goodname like '%" + name + "%'"
        if count or count2:
            if s:
                s += " and "
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
        self.model.setFilter(s)
        if self.chkDesc.isChecked():
            o = QtCore.Qt.SortOrder.DescendingOrder
        else:
            o = QtCore.Qt.SortOrder.AscendingOrder
        self.model.setSort(self.cboSort.currentIndex() + 1, o)
        self.model.select()

    def _addRecord(self):
        self.model.insertRow(self.model.rowCount())

    def _delRecord(self):
        result = QtWidgets.QMessageBox.warning(window,
            "Работа с данными", "Удалить запись?",
            buttons=QtWidgets.QMessageBox.StandardButton.Yes |
                    QtWidgets.QMessageBox.StandardButton.No,
            defaultButton=QtWidgets.QMessageBox.StandardButton.No)
        if result == QtWidgets.QMessageBox.StandardButton.Yes:
            self.model.removeRow(self.tblMain.currentIndex().row())
            self.model.select()

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
