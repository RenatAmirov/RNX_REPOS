from PyQt6 import QtCore, QtWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window)
        self.setWindowTitle("Использование ключей")
        self.settings = QtCore.QSettings("Прохоренок и Дронов",
                                         "Использование ключей")
        vbox = QtWidgets.QVBoxLayout()
        self.txtLine = QtWidgets.QLineEdit(parent=self)
        vbox.addWidget(self.txtLine)
        btnSave = QtWidgets.QPushButton("&Сохранить текст")
        btnSave.clicked.connect(self.saveText)
        vbox.addWidget(btnSave)
        self.setLayout(vbox)
        if self.settings.contains("Окно/Местоположение"):
            self.setGeometry(self.settings.value("Окно/Местоположение"))
        else:
            self.resize(200, 50)
        if self.settings.contains("Данные/Текст"):
            self.txtLine.setText(self.settings.value("Данные/Текст"))

    def closeEvent(self, evt):
        self.settings.beginGroup("Окно")
        self.settings.setValue("Местоположение", self.geometry())
        self.settings.endGroup()

    def saveText(self):
        self.settings.beginGroup("Данные")
        self.settings.setValue("Текст", self.txtLine.text())
        self.settings.endGroup()

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
