from PyQt6 import QtWidgets
import sys

class MyLabel(QtWidgets.QLabel):
    def __init__(self, text, parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
    
    def heightForWidth(self, w):
        return w // 2

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QSizePolicy")
window.resize(300, 250)
label = MyLabel("Минимальная высота компонента зависит от ширины")
button = QtWidgets.QPushButton("1")

label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                    QtWidgets.QFrame.Shadow.Plain)
policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, 
                               QtWidgets.QSizePolicy.Policy.Expanding)
policy.setHeightForWidth(True)
label.setSizePolicy(policy)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(button)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
