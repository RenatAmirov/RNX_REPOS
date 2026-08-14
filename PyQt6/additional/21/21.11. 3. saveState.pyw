from PyQt6 import QtCore, QtWidgets
import sys

state = None

def on_clicked_button1():
    global state
    state = splitter.saveState()
    button2.setEnabled(True)

def on_clicked_button2():
    global state
    splitter.restoreState(state)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QSplitter")
window.resize(300, 350)
button1 = QtWidgets.QPushButton("Запомнить размеры")
button2 = QtWidgets.QPushButton("Восстановить размеры")
button1.clicked.connect(on_clicked_button1)
button2.clicked.connect(on_clicked_button2)
button2.setEnabled(False)
splitter = QtWidgets.QSplitter(QtCore.Qt.Orientation.Vertical)
label1 = QtWidgets.QLabel("Содержимое компонента 1")
label2 = QtWidgets.QLabel("Содержимое компонента 2")
label1.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                     QtWidgets.QFrame.Shadow.Plain)
label2.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                     QtWidgets.QFrame.Shadow.Plain)
splitter.addWidget(label1)
splitter.addWidget(label2)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(splitter)
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
