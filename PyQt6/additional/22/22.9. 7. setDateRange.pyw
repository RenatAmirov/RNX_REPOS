from PyQt6 import QtWidgets
import sys, datetime

def on_clicked():
    print(dateTimeEdit.dateTime().toPyDateTime())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QDateTimeEdit")
window.resize(300, 70)
dateTimeEdit = QtWidgets.QDateTimeEdit()
dt = datetime.datetime.today()
delta = datetime.timedelta(days=365, hours=5)
dt_min = dt - delta
dt_max = dt + delta
dateTimeEdit.setDateTime(dt)
dateTimeEdit.setDateRange(dt_min.date(), dt_max.date())
dateTimeEdit.setTimeRange(dt_min.time(), dt_max.time())
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(dateTimeEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
