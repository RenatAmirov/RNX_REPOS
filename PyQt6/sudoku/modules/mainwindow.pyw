from PyQt6 import QtCore, QtGui, QtWidgets, QtPrintSupport
import re
from modules.widget import Widget
from modules.previewdialog import PreviewDialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent,
                  flags=QtCore.Qt.WindowType.Window |
                        QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Судоку 2.0.0")
        self.setStyleSheet(
             "QFrame QPushButton {font-size:10pt;font-family:Verdana;"
             "color:black;font-weight:bold;}"
             "MyLabel {font-size:14pt;font-family:Verdana;"
             "border:1px solid #9AA6A7;}")
        self.settings = QtCore.QSettings("Прохоренок и Дронов", "Судоку")
        self.printer = QtPrintSupport.QPrinter()
        self.sudoku = Widget()
        self.setCentralWidget(self.sudoku)
        menuBar = self.menuBar()
        toolBar = QtWidgets.QToolBar()
        myMenuFile = menuBar.addMenu("&Файл")
        action = myMenuFile.addAction(QtGui.QIcon(r"images/new.png"),
                            "&Новый", self.sudoku.onClearAllCells,
                            QtGui.QKeySequence("Ctrl+N"))
        toolBar.addAction(action)
        action.setStatusTip("Создание новой, пустой головоломки")

        action = myMenuFile.addAction(QtGui.QIcon(r"images/open.png"),
                            "&Открыть...", self.onOpenFile,
                            QtGui.QKeySequence("Ctrl+O"))
        toolBar.addAction(action)
        action.setStatusTip("Загрузка головоломки из файла")

        action = myMenuFile.addAction(QtGui.QIcon(r"images/save.png"),
                            "Со&хранить...", self.onSave,
                            QtGui.QKeySequence("Ctrl+S"))
        toolBar.addAction(action)
        action.setStatusTip("Сохранение головоломки в файле")

        action = myMenuFile.addAction("&Сохранить компактно...",
                                      self.onSaveMini)
        action.setStatusTip("Сохранение головоломки в компактном формате")

        myMenuFile.addSeparator()
        toolBar.addSeparator()

        action = myMenuFile.addAction(QtGui.QIcon(r"images/print.png"),
                            "&Печать...", self.onPrint,
                            QtGui.QKeySequence("Ctrl+P"))
        toolBar.addAction(action)
        action.setStatusTip("Печать головоломки")

        action = myMenuFile.addAction(QtGui.QIcon(r"images/preview.png"),
                            "П&редварительный просмотр...", self.onPreview)
        toolBar.addAction(action)
        action.setStatusTip("Предварительный просмотр головоломки")
        action = myMenuFile.addAction("П&араметры страницы...",
                            self.onPageSetup)
        action.setStatusTip("Задание параметров страницы")

        myMenuFile.addSeparator()
        toolBar.addSeparator()

        action = myMenuFile.addAction("&Выход",
                            QtWidgets.QApplication.instance().quit,
                            QtGui.QKeySequence("Ctrl+Q"))
        action.setStatusTip("Завершение работы программы")
        
        myMenuEdit = menuBar.addMenu("&Правка")

        action = myMenuEdit.addAction(QtGui.QIcon(r"images/copy.png"),
                            "К&опировать", self.onCopyData,
                            QtGui.QKeySequence("Ctrl+C"))
        toolBar.addAction(action)
        action.setStatusTip("Копирование головоломки в буфер обмена")

        action = myMenuEdit.addAction("&Копировать компактно",
                                      self.onCopyDataMini)
        action.setStatusTip("Копирование в компактном формате")

        action = myMenuEdit.addAction("Копировать &для Excel",
                            self.onCopyDataExcel)
        action.setStatusTip("Копирование в формате MS Excel")

        action = myMenuEdit.addAction(QtGui.QIcon(r"images/paste.png"),
                            "&Вставить", self.onPasteData,
                            QtGui.QKeySequence("Ctrl+V"))
        toolBar.addAction(action)
        action.setStatusTip("Вставка головоломки из буфера обмена")

        action = myMenuEdit.addAction("Вставить &из Excel",
                            self.onPasteDataExcel)
        action.setStatusTip("Вставка головоломки из MS Excel")

        myMenuEdit.addSeparator()
        toolBar.addSeparator()

        action = myMenuEdit.addAction("&Блокировать",
                            self.sudoku.onBlockCell, QtCore.Qt.Key.Key_F2)
        action.setStatusTip("Блокирование активной ячейки")
        action = myMenuEdit.addAction(QtGui.QIcon(r"images/lock.png"),
                            "Б&локировать все",
                            self.sudoku.onBlockCells, QtCore.Qt.Key.Key_F3)
        toolBar.addAction(action)
        action.setStatusTip("Блокирование всех ячеек")

        action = myMenuEdit.addAction("&Разблокировать",
                            self.sudoku.onClearBlockCell, QtCore.Qt.Key.Key_F4)
        action.setStatusTip("Разблокирование активной ячейки")

        action = myMenuEdit.addAction(QtGui.QIcon(r"images/unlock.png"),
                            "Р&азблокировать все",
                            self.sudoku.onClearBlockCells,
                            QtCore.Qt.Key.Key_F5)
        toolBar.addAction(action)
        action.setStatusTip("Разблокирование всех ячеек")
        myMenuAbout = menuBar.addMenu("&Справка")

        action = myMenuAbout.addAction("О &программе...", self.aboutProgram)
        action.setStatusTip("Получение сведений о программе")

        action = myMenuAbout.addAction("О &Qt...", self.aboutQt)
        action.setStatusTip("Получение сведений о фреймворке Qt")
        toolBar.setMovable(False)
        toolBar.setFloatable(False)
        self.addToolBar(toolBar)
        statusBar = self.statusBar()
        statusBar.setSizeGripEnabled(False)
        statusBar.showMessage("\"Судоку\" приветствует вас", 20000)
        if self.settings.contains("X") and self.settings.contains("Y"):
            self.move(self.settings.value("X"), self.settings.value("Y"))

    def closeEvent(self, evt):
        g = self.geometry()
        self.settings.setValue("X", g.left())
        self.settings.setValue("Y", g.top())

    def aboutProgram(self):
        QtWidgets.QMessageBox.about(self, "О программе",
                  "<center>\"Судоку\" v2.0.0<br><br>"
                  "Программа для просмотра и редактирования судоку<br><br>"
                  "(c) Прохоренок Н.А., Дронов В.А. 2011-2022 гг.")

    def aboutQt(self):
        QtWidgets.QMessageBox.aboutQt(self, title="О фреймворке Qt")

    def onCopyData(self):
        QtWidgets.QApplication.clipboard().setText(
            self.sudoku.getDataAllCells())

    def onCopyDataMini(self):
        QtWidgets.QApplication.clipboard().setText(
            self.sudoku.getDataAllCellsMini())

    def onCopyDataExcel(self):
        QtWidgets.QApplication.clipboard().setText(
            self.sudoku.getDataAllCellsExcel())

    def onPasteData(self):
        data = QtWidgets.QApplication.clipboard().text()
        if data:
            if len(data) == 81 or len(data) == 162:
                r = re.compile(r"[^0-9]")
                if not r.match(data):
                    self.sudoku.setDataAllCells(data)
                    return
        self.dataErrorMsg()

    def onPasteDataExcel(self):
        data = QtWidgets.QApplication.clipboard().text()
        if data:
            data = data.replace("\r", "")
            r = re.compile(r"([0-9]?[\t\n]){81}")
            if r.match(data):
                result = []
                if data[-1] == "\n":
                    data = data[:-1]
                dl = data.split("\n")
                for sl in dl:
                    dli = sl.split("\t")
                    for sli in dli:
                        if len(sli) == 0:
                            result.append("00")
                        else:
                            result.append("0" + sli[0])
                data = "".join(result)
                self.sudoku.setDataAllCells(data)
                return
        self.dataErrorMsg()

    def dataErrorMsg(self):
        QtWidgets.QMessageBox.information(self, "Судоку",
                  "Данные имеют неправильный формат")

    def onOpenFile(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self,
                   "Выберите файл", QtCore.QDir.homePath(),
                   "Судоку (*.svd)")[0]
        if fileName:
            data = ""
            try:
                with open(fileName, newline="") as f:
                    data = f.read()
            except:
                QtWidgets.QMessageBox.information(self, "Судоку",
                          "Не удалось открыть файл")
                return
            if len(data) > 2:
                if data[-1] == "\n":
                    data = data[:-1]
                if len(data) == 81 or len(data) == 162:
                    r = re.compile(r"[^0-9]")
                    if not r.match(data):
                        self.sudoku.setDataAllCells(data)
                        return
            self.dataErrorMsg()

    def onSave(self):
        self.saveSVDFile(self.sudoku.getDataAllCells())

    def onSaveMini(self):
        self.saveSVDFile(self.sudoku.getDataAllCellsMini())

    def saveSVDFile(self, data):
        fileName = QtWidgets.QFileDialog.getSaveFileName(self,
                   "Выберите файл", QtCore.QDir.homePath(),
                   "Судоку (*.svd)")[0]
        if fileName:
            try:
                with open(fileName, mode="w", newline="") as f:
                    f.write(data)
                self.statusBar().showMessage("Файл сохранен", 10000)
            except:
                QtWidgets.QMessageBox.information(self, "Судоку",
                          "Не удалось сохранить файл")

    def onPrint(self):
        pd = QtPrintSupport.QPrintDialog(self.printer, parent=self)
        pd.setOptions(
              QtPrintSupport.QPrintDialog.PrintDialogOption.PrintToFile |
              QtPrintSupport.QPrintDialog.PrintDialogOption.PrintSelection)
        if pd.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            self.sudoku.print(self.printer)

    def onPreview(self):
        pd = PreviewDialog(self)
        pd.exec()

    def onPageSetup(self):
        pd = QtPrintSupport.QPageSetupDialog(self.printer, parent=self)
        pd.exec()
