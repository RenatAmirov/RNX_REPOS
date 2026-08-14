from PyQt6 import QtCore, QtWidgets
import sys, datetime

def on_clicked():
    print(calendar.selectedDate().toPyDate())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QCalendarWidget")
window.resize(300, 200)
calendar = QtWidgets.QCalendarWidget()
calendar.setSelectedDate(datetime.date.today())
calendar.setFirstDayOfWeek(QtCore.Qt.DayOfWeek.Monday)
calendar.setHorizontalHeaderFormat(
    QtWidgets.QCalendarWidget.HorizontalHeaderFormat.NoHorizontalHeader)
button = QtWidgets.QPushButton("Вывести значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(calendar)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
