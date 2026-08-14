from PyQt6 import QtWidgets
import sys

def on_clicked():
    wizard = QtWidgets.QWizard(window)
    wizard.setWindowTitle("Мой мастер")
    
    page1 = QtWidgets.QWizardPage()
    page1.setTitle("Название страницы 1")
    label1 = QtWidgets.QLabel("Содержимое страницы 1")
    line1 = QtWidgets.QLineEdit()
    box1 = QtWidgets.QVBoxLayout()
    box1.addWidget(label1)
    box1.addWidget(line1)
    page1.setLayout(box1)
    page1.registerField("line1*", line1)
    
    page2 = QtWidgets.QWizardPage()
    page2.setTitle("Название страницы 2")
    page2.setSubTitle("Подзаголовок на странице 2")
    label2 = QtWidgets.QLabel("Содержимое страницы 2")
    line2 = QtWidgets.QLineEdit()
    box2 = QtWidgets.QVBoxLayout()
    box2.addWidget(label2)
    box2.addWidget(line2)
    page2.setLayout(box2)
    page2.registerField("line2*", line2)
    
    wizard.addPage(page1)
    wizard.setPage(1, page2)

    result = wizard.exec()
    if result == QtWidgets.QDialog.DialogCode.Accepted:
        print("Нажата кнопка Finish")
        print(line1.text(), wizard.field("line1"))
        print(line2.text(), wizard.field("line2"))
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
