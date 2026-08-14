from PyQt6 import QtWidgets
import sys, datetime

def on_clicked():
    print(dateTimeEdit.dateTime().toPyDateTime())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QDateTimeEdit")
window.resize(300, 70)
dateTimeEdit = QtWidgets.QDateTimeEdit(datetime.datetime.today())
dateTimeEdit.setDisplayFormat("дата: dd.MM.yyyy, время: HH:mm:ss")
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(dateTimeEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
