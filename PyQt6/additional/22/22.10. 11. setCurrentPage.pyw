from PyQt6 import QtWidgets
import sys, datetime

def on_clicked():
    print(calendar.selectedDate().toPyDate())
    print(calendar.yearShown(), calendar.monthShown())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QCalendarWidget")
window.resize(300, 70)
calendar = QtWidgets.QCalendarWidget()
calendar.setSelectedDate(datetime.date.today())
calendar.setCurrentPage(2021, 12)
button = QtWidgets.QPushButton("Вывести значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(calendar)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
