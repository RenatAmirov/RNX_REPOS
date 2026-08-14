from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLabel")
window.resize(300, 150)
label = QtWidgets.QLabel()
label.setText("Этот текст можно редактировать")
label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                    QtWidgets.QFrame.Shadow.Plain)
label.setTextInteractionFlags(
             QtCore.Qt.TextInteractionFlag.TextEditorInteraction)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
