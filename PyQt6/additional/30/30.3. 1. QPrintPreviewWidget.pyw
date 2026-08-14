from PyQt6 import QtCore, QtWidgets, QtPrintSupport, QtGui
import sys
import PrintList

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window)
        self.setWindowTitle("Класс QPrintPreviewWidget")
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        self.btnPortrait = QtWidgets.QPushButton("Порт&рет")
        hbox.addWidget(self.btnPortrait)
        self.btnLandscape = QtWidgets.QPushButton("&Ландшафт")
        hbox.addWidget(self.btnLandscape)
        hbox.addStretch()
        self.btnZoomIn = QtWidgets.QPushButton("&Крупнее")
        hbox.addWidget(self.btnZoomIn)
        self.btnZoomOut = QtWidgets.QPushButton("&Мельче")
        hbox.addWidget(self.btnZoomOut)
        hbox.addStretch()
        lblPage = QtWidgets.QLabel("Стр.")
        hbox.addWidget(lblPage, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        self.spnPage = QtWidgets.QSpinBox()
        self.spnPage.setMinimum(1)
        self.spnPage.setValue(1)
        hbox.addWidget(self.spnPage)
        hbox.addStretch()
        self.btnPrint = QtWidgets.QPushButton("&Печать...")
        hbox.addWidget(self.btnPrint)
        vbox.addLayout(hbox)
        self.printer = QtPrintSupport.QPrinter()
        self.printer.setPageOrientation(
                        QtGui.QPageLayout.Orientation.Portrait)
        self.ppwMain = QtPrintSupport.QPrintPreviewWidget(self.printer)
        self.ppwMain.paintRequested.connect(self.printData)
        self.ppwMain.previewChanged.connect(self.refresh)
        vbox.addWidget(self.ppwMain)
        self.btnPortrait.clicked.connect(
                                 self.ppwMain.setPortraitOrientation)
        self.btnLandscape.clicked.connect(
                                  self.ppwMain.setLandscapeOrientation)
        self.btnZoomIn.clicked.connect(self.ppwMain.zoomIn)
        self.btnZoomOut.clicked.connect(self.ppwMain.zoomOut)
        self.spnPage.valueChanged[int].connect(
                                       self.ppwMain.setCurrentPage)
        self.btnPrint.clicked.connect(self.ppwMain.print)
        self.setLayout(vbox)
        self.resize(500, 700)

    def printData(self, printer):
        painter = QtGui.QPainter()
        pl = PrintList.PrintList()
        data = []
        for b in range(1, 101):
            data.append([b, b ** 2, b ** 3])
        pl.printer = printer
        pl.data = data
        pl.columnWidths = [100, 100, 200]
        pl.headers = ["Аргумент", "Квадрат", "Куб"]
        pl.printData()

    def refresh(self):
        self.spnPage.setMaximum(self.ppwMain.pageCount())

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
