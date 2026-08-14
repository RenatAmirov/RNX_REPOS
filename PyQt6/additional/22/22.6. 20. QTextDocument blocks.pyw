from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    print(textEdit.document().firstBlock().text())
    print(textEdit.document().lastBlock().text())
    print(textEdit.document().findBlock(0).text())
    print(textEdit.document().findBlockByNumber(4).text())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
document = QtGui.QTextDocument()
document.setPlainText("Блок 1\nБлок 2\nБлок 3\nБлок 4\nБлок 5")
textEdit.setDocument(document)
button = QtWidgets.QPushButton("Получить значения")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
