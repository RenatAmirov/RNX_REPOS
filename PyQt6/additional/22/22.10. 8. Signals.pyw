from PyQt6 import QtCore, QtWidgets
import sys, datetime

def on_clicked():
    print(calendar.selectedDate().toPyDate())

def on_activated(d):
    print("on_activated -", d.toPyDate())

def on_clicked_calendar(d):
    print("on_clicked_calendar -", d.toPyDate())

def on_page_changed(y, m):
    print("on_page_changed -", y, m)

def on_selection_changed():
    print("on_selection_changed")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QCalendarWidget")
window.resize(300, 200)
calendar = QtWidgets.QCalendarWidget()
calendar.setSelectedDate(datetime.date.today())
calendar.setFirstDayOfWeek(QtCore.Qt.DayOfWeek.Monday)
calendar.activated["QDate"].connect(on_activated)
calendar.clicked["QDate"].connect(on_clicked_calendar)
calendar.currentPageChanged[int, int].connect(on_page_changed)
calendar.selectionChanged.connect(on_selection_changed)
button = QtWidgets.QPushButton("Вывести значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(calendar)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
