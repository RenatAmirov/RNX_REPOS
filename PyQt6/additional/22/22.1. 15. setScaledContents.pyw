from PyQt6 import QtCore, QtGui, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLabel")
window.resize(300, 150)
label = QtWidgets.QLabel()
label.setText("Текст надписи")
label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                    QtWidgets.QFrame.Shadow.Plain)
label.setPixmap(QtGui.QPixmap("photo.jpg"))
label.setAutoFillBackground(True)
label.setScaledContents(True)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
