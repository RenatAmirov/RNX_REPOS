from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QSplitter")
window.resize(250, 200)
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
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
