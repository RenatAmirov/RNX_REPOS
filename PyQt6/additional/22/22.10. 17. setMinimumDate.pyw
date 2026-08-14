from PyQt6 import QtWidgets
import sys, datetime

def on_clicked():
    print(calendar.selectedDate().toPyDate())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QCalendarWidget")
window.resize(300, 70)
calendar = QtWidgets.QCalendarWidget()
d = datetime.date.today()
d_min = d - datetime.timedelta(days=60)
d_max = d + datetime.timedelta(days=60)
calendar.setMinimumDate(d_min)
calendar.setMaximumDate(d_max)
button = QtWidgets.QPushButton("Вывести значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(calendar)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
