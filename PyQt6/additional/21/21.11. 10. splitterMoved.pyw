from PyQt6 import QtCore, QtWidgets
import sys

def on_moved(x, y):
    print(x, y)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QSplitter")
window.resize(300, 350)
splitter = QtWidgets.QSplitter(QtCore.Qt.Orientation.Vertical)
label1 = QtWidgets.QLabel("Содержимое компонента 1")
label2 = QtWidgets.QLabel("Содержимое компонента 2")
label3 = QtWidgets.QLabel("Содержимое компонента 3")
label1.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                     QtWidgets.QFrame.Shadow.Plain)
label2.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                     QtWidgets.QFrame.Shadow.Plain)
label3.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                     QtWidgets.QFrame.Shadow.Plain)
splitter.addWidget(label1)
splitter.addWidget(label2)
splitter.addWidget(label3)
splitter.splitterMoved["int", "int"].connect(on_moved)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(splitter)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
