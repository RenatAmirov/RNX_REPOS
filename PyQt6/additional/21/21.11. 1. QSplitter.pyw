from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QSplitter")
window.resize(400, 250)
splitter = QtWidgets.QSplitter(QtCore.Qt.Orientation.Vertical)
splitter2 = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal)
label1 = QtWidgets.QLabel("Содержимое 1")
label2 = QtWidgets.QLabel("Содержимое 2")
label3 = QtWidgets.QLabel("Содержимое 3")
label1.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                     QtWidgets.QFrame.Shadow.Plain)
label2.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                     QtWidgets.QFrame.Shadow.Plain)
label3.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                     QtWidgets.QFrame.Shadow.Plain)
splitter2.addWidget(label1)
splitter2.addWidget(label2)
splitter.addWidget(splitter2)
splitter.addWidget(label3)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(splitter)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
