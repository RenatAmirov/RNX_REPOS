from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QFrame")
window.resize(300, 250)
frame1 = QtWidgets.QFrame()
frame2 = QtWidgets.QFrame()
frame3 = QtWidgets.QFrame()
frame1.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                     QtWidgets.QFrame.Shadow.Plain)
frame2.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                     QtWidgets.QFrame.Shadow.Raised)
frame3.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                     QtWidgets.QFrame.Shadow.Sunken)
frame1.setLineWidth(5)
frame2.setLineWidth(5)
frame3.setLineWidth(5)
frame1.setMidLineWidth(10)
frame2.setMidLineWidth(10)
frame3.setMidLineWidth(10)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(frame1)
vbox.addWidget(frame2)
vbox.addWidget(frame3)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
