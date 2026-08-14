from PyQt6 import QtCore, QtWidgets, QtGui
import sys

def on_clicked():
    rx = QtCore.QRegularExpression("Т[А-Я]+Т")
    rx.setPatternOptions(
          QtCore.QRegularExpression.PatternOption.CaseInsensitiveOption)
    cursor = textEdit.document().find(rx, position=0)
    if not cursor.isNull():
        textEdit.setTextCursor(cursor)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
document = QtGui.QTextDocument()
document.setPlainText("текст\nтекст\nТЕКСТ\nтекст\nтекст\nтекст\nтекст"
                      "\nтекст\nтекст\nтекст\n")
textEdit.setDocument(document)
button = QtWidgets.QPushButton("Поиск фрагмента")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
