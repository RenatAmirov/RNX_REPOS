from PyQt6 import QtWidgets, QtGui
import sys

def on_clicked():
    textEdit.document().setModified(False)

def on_block_count_changed(cnt):
    print("on_block_count_changed", cnt)

def on_undo(status):
    print("on_undo", status)

def on_redo(status):
    print("on_redo", status)

def on_contents_changed():
    print("on_contents_changed")

def on_contents_change(x, y, z):
    print("on_contents_change", x, y, z)

def on_position_changed(cur):
    print("on_position_changed")

def on_modification_changed(status):
    print("on_modification_changed", status)

def on_undo_command_added():
    print("on_undo_command_added")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextDocument")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit()
document = QtGui.QTextDocument()
document.blockCountChanged[int].connect(on_block_count_changed)
document.undoAvailable[bool].connect(on_undo)
document.redoAvailable[bool].connect(on_redo)
document.contentsChanged.connect(on_contents_changed)
document.contentsChange[int, int, int].connect(on_contents_change)
document.cursorPositionChanged["QTextCursor"].connect(
    on_position_changed)
document.modificationChanged[bool].connect(on_modification_changed)
document.undoCommandAdded.connect(on_undo_command_added)
textEdit.setDocument(document)
button = QtWidgets.QPushButton("Изменить статус документа")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
