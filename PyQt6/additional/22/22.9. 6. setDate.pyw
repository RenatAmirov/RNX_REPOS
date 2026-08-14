from PyQt6 import QtWidgets
import sys, datetime

def on_clicked():
    print(dateTimeEdit.date().toPyDate())
    print(dateTimeEdit.time().toPyTime())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QDateTimeEdit")
window.resize(300, 70)
dateTimeEdit = QtWidgets.QDateTimeEdit()
dt = datetime.datetime.today()
dateTimeEdit.setDate(dt.date())
dateTimeEdit.setTime(dt.time())
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(dateTimeEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
