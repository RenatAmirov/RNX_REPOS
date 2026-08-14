from PyQt6 import QtCore, QtWidgets
import sys

class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle("Диалоговое окно")
        self.resize(200, 70)
        
        self.mainBox = QtWidgets.QVBoxLayout()
        
        self.lineEdit = QtWidgets.QLineEdit()
        self.mainBox.addWidget(self.lineEdit)
        
        self.hbox = QtWidgets.QHBoxLayout()
        self.btnOK = QtWidgets.QPushButton("&OK")
        self.btnCancel = QtWidgets.QPushButton("&Cancel")
        self.btnCancel.setDefault(True)
        self.btnCancel.clicked.connect(self.hide)
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)
        
        self.setLayout(self.mainBox)

def on_clicked():
    if not dialog.isVisible():
        dialog.lineEdit.setText("")
        dialog.show()
        dialog.raise_()
        dialog.activateWindow()

def on_accept():
    dialog.hide()
    print(dialog.lineEdit.text())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QDialog")
window.resize(300, 70)

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

window2 = QtWidgets.QWidget()
window2.setWindowTitle("Это окно не будет блокировано при WindowModal")
window2.resize(500, 100)
window2.show()

dialog = MyDialog(window)
dialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
dialog.btnOK.clicked.connect(on_accept)
dialog.hide()

sys.exit(app.exec())
