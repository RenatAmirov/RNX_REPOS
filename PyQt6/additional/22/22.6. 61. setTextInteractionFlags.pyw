from PyQt6 import QtCore, QtWidgets
import sys

flag = 1
allFlags = [QtCore.Qt.TextInteractionFlag.NoTextInteraction,
            QtCore.Qt.TextInteractionFlag.TextSelectableByMouse,
            QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard,
            QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse,
            QtCore.Qt.TextInteractionFlag.LinksAccessibleByKeyboard,
            QtCore.Qt.TextInteractionFlag.TextEditable,
            QtCore.Qt.TextInteractionFlag.TextEditorInteraction,
            QtCore.Qt.TextInteractionFlag.TextBrowserInteraction]

def on_clicked():
    global flag
    textEdit.setTextInteractionFlags(allFlags[flag])
    flag += 1
    if flag > 7:
        flag = 0

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextEdit")
window.resize(500, 250)
textEdit = QtWidgets.QTextEdit("""Значение по умолчанию <a href="https://www.google.ru/">ссылка</a>""")
textEdit.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.NoTextInteraction)
button = QtWidgets.QPushButton("Переключить режим")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(textEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
