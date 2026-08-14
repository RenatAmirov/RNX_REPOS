from PyQt6 import QtCore, QtWidgets
import sys

def on_clicked():
    print(label.hasSelectedText())
    label.setSelection(3, 10)
    print(label.hasSelectedText())
    print(label.selectedText())
    print(label.selectionStart())
    label.setFocus()

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLabel")
window.resize(300, 150)
button = QtWidgets.QPushButton("Выделить текст")
button.clicked.connect(on_clicked)
label = QtWidgets.QLabel()
label.setText("Этот текст можно выделить")
label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                    QtWidgets.QFrame.Shadow.Plain)
label.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
label.setTextInteractionFlags(
         QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
