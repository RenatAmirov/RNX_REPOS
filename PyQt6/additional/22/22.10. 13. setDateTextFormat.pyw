from PyQt6 import QtCore, QtWidgets, QtGui
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
f = QtGui.QTextCharFormat()
f.setFont(QtGui.QFont("Tahoma", 16, QtGui.QFont.Weight.Bold))
f.setBackground(QtGui.QBrush(QtGui.QColor("#008800")))
d = datetime.date.today() - datetime.timedelta(days=5)
calendar.setDateTextFormat(d, f)
button = QtWidgets.QPushButton("Вывести значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(calendar)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
