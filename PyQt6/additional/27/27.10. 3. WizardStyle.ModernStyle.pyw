from PyQt6 import QtWidgets
import sys

class MyPage1(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.setTitle("Название страницы 1")
        self.label1 = QtWidgets.QLabel("Содержимое страницы 1")
        self.line1 = QtWidgets.QLineEdit()
        self.box1 = QtWidgets.QVBoxLayout()
        self.box1.addWidget(self.label1)
        self.box1.addWidget(self.line1)
        self.setLayout(self.box1)
        self.registerField("line1*", self.line1)

class MyPage2(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.setTitle("Название страницы 2")
        self.setSubTitle("Текст подзаголовка")
        self.label2 = QtWidgets.QLabel("Содержимое страницы 2")
        self.line2 = QtWidgets.QLineEdit()
        self.box2 = QtWidgets.QVBoxLayout()
        self.box2.addWidget(self.label2)
        self.box2.addWidget(self.line2)
        self.setLayout(self.box2)
        self.registerField("line2*", self.line2)

class MyPage3(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        QtWidgets.QWizardPage.__init__(self, parent)
        self.setTitle("Название страницы 3")
        self.setSubTitle("Текст подзаголовка")
        self.label3 = QtWidgets.QLabel("Содержимое страницы 3")
        self.line3 = QtWidgets.QLineEdit()
        self.box3 = QtWidgets.QVBoxLayout()
        self.box3.addWidget(self.label3)
        self.box3.addWidget(self.line3)
        self.setLayout(self.box3)
        self.registerField("line3*", self.line3)

class MyWizard(QtWidgets.QWizard):
    def __init__(self, parent=None):
        QtWidgets.QWizard.__init__(self, parent)
        self.setWindowTitle("Мой мастер")
        self.setWizardStyle(QtWidgets.QWizard.WizardStyle.ModernStyle)

        self.page1 = MyPage1()
        self.page2 = MyPage2()
        self.page3 = MyPage3()
        self.idPage1 = self.addPage(self.page1)
        self.idPage2 = self.addPage(self.page2)
        self.idPage3 = self.addPage(self.page3)
        

def on_clicked():
    wizard = MyWizard(window)
    result = wizard.exec()
    if result == QtWidgets.QDialog.DialogCode.Accepted:
        print("Нажата кнопка Finish")
        print(wizard.field("line1"))
        print(wizard.field("line2"))
        print(wizard.field("line3"))
    else:
        print("Нажата кнопка Cancel, кнопка Закрыть или клавиша <Esc>", 
              result)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QWizard")
window.resize(300, 70)

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec())
