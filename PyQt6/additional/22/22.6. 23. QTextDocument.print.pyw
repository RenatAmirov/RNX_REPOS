from PyQt6 import QtWidgets, QtGui, QtPrintSupport
import sys

def on_clicked():
    printer = QtPrintSupport.QPrinter()
    printer.setOutputFormat(QtPrintSupport.QPrinter.OutputFormat.PdfFormat)
    printer.setOutputFileName("mypdf.pdf")
    textEdit.document().print(printer)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
document = QtGui.QTextDocument()
document.setPlainText("текст\nтекст\nТЕКСТ\nтекст\nтекст\nтекст\nтекст"
                      "\nтекст\nтекст\nтекст\n")
textEdit.setDocument(document)
button = QtWidgets.QPushButton("Печать в PDF")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
