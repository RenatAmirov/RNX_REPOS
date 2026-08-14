from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    f = QtGui.QTextCharFormat()
    f.setFontUnderline(True)
    textEdit.setCurrentCharFormat(f)

def on_copy(status):
    print("on_copy", status)

def on_undo(status):
    print("on_undo", status)

def on_redo(status):
    print("on_redo", status)

def on_format_changed(s):
    print("on_format_changed")

def on_position_changed():
    print("on_position_changed")

def on_selection_changed():
    print("on_selection_changed")

def on_text_changed():
    print("on_text_changed")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit("Значение по умолчанию")
textEdit.copyAvailable["bool"].connect(on_copy)
textEdit.undoAvailable["bool"].connect(on_undo)
textEdit.redoAvailable["bool"].connect(on_redo)
textEdit.currentCharFormatChanged.connect(on_format_changed)
textEdit.cursorPositionChanged.connect(on_position_changed)
textEdit.selectionChanged.connect(on_selection_changed)
textEdit.textChanged.connect(on_text_changed)
button = QtWidgets.QPushButton("Подчеркнуть текст")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
