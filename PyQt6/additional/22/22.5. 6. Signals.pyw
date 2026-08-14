from PyQt6 import QtWidgets
import sys

def on_clicked():
    lineEdit.setText("Новый текст")

def on_changed(old_pos, new_pos):
    print("on_changed", old_pos, new_pos)

def on_finished():
    print("on_finished")

def on_return():
    print("on_return")

def on_selection():
    print("on_selection")

def on_text_changed(s):
    print("on_text_changed", s)

def on_text_edited(s):
    print("on_text_edited", s)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLineEdit")
window.resize(300, 100)
lineEdit = QtWidgets.QLineEdit()
lineEdit.cursorPositionChanged["int","int"].connect(on_changed)
lineEdit.editingFinished.connect(on_finished)
lineEdit.returnPressed.connect(on_return)
lineEdit.selectionChanged.connect(on_selection)
lineEdit.selectionChanged.connect(on_selection)
lineEdit.textChanged.connect(on_text_changed)
lineEdit.textEdited.connect(on_text_edited)
lineEdit2 = QtWidgets.QLineEdit()
button = QtWidgets.QPushButton("Изменить текст программно")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(lineEdit)
box.addWidget(lineEdit2)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
