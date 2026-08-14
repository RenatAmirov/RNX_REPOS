from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLabel")
window.resize(300, 80)
label = QtWidgets.QLabel()
label.setText("Текст надписи")
#label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft |
#                   QtCore.Qt.AlignmentFlag.AlignBottom)
#label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter |
#                   QtCore.Qt.AlignmentFlag.AlignBottom)
#label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
#                   QtCore.Qt.AlignmentFlag.AlignBottom)
label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                    QtWidgets.QFrame.Shadow.Plain)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
