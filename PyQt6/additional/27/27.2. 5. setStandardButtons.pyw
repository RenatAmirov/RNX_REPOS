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
        
        self.box = QtWidgets.QDialogButtonBox()
        self.box.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.box.setCenterButtons(True)
        self.box.setStandardButtons(
                    QtWidgets.QDialogButtonBox.StandardButton.Ok |
                    QtWidgets.QDialogButtonBox.StandardButton.Cancel | 
                    QtWidgets.QDialogButtonBox.StandardButton.Help)
        self.box.accepted.connect(self.accept)
        self.box.rejected.connect(self.reject)
        self.box.helpRequested.connect(self.on_help_requested)
        self.box.clicked["QAbstractButton *"].connect(
                                    self.on_btn_clicked)

        self.mainBox.addWidget(self.box)

        self.setLayout(self.mainBox)

    def on_help_requested(self):
        print("Нажата кнопка с ролью HelpRole")

    def on_btn_clicked(self, btn):
        if btn:
            print("Нажата кнопка", btn.text())

def on_clicked():
    dialog = MyDialog(window)
    dialog.box.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).\
               setDefault(True)
    result = dialog.exec()
    if result == QtWidgets.QDialog.DialogCode.Accepted:
        print(dialog.lineEdit.text())
    else:
        print("Нажата кнопка Cancel, кнопка Закрыть или клавиша <Esc>", 
              result)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QDialogButtonBox")
window.resize(300, 70)

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec())
