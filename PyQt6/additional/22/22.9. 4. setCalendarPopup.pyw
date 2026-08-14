from PyQt6 import QtWidgets
import sys, datetime

def on_clicked():
    print(dateTimeEdit.dateTime().toPyDateTime())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QDateTimeEdit")
window.resize(300, 70)
dt = datetime.datetime.today()
delta = datetime.timedelta(days=365)
dt_min = dt - delta
dt_max = dt + delta
dateTimeEdit = QtWidgets.QDateTimeEdit(dt.date())
dateTimeEdit.setDateRange(dt_min.date(), dt_max.date())
dateTimeEdit.setCalendarPopup(True)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(dateTimeEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
