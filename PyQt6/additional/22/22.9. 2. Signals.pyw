from PyQt6 import QtWidgets
import sys, datetime

def on_clicked():
    print(dateTimeEdit.dateTime().toPyDateTime())

def on_date_time_changed(d):
    print("on_date_time_changed -", d.toPyDateTime())

def on_date_changed(d):
    print("on_date_changed -", d.toPyDate())

def on_time_changed(t):
    print("on_time_changed -", t.toPyTime())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QDateTimeEdit")
window.resize(300, 70)
dateTimeEdit = QtWidgets.QDateTimeEdit(datetime.datetime.today())
dateTimeEdit.dateTimeChanged["QDateTime"].connect(on_date_time_changed)
dateTimeEdit.dateChanged["QDate"].connect(on_date_changed)
dateTimeEdit.timeChanged["QTime"].connect(on_time_changed)
button = QtWidgets.QPushButton("Вывести значения")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(dateTimeEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
