from PyQt6 import QtWidgets
import sys, datetime

def on_clicked():
    dateTimeEdit.setFocus()
    dateTimeEdit.setCurrentSection(
                    QtWidgets.QDateTimeEdit.Section.YearSection)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QDateTimeEdit")
window.resize(300, 70)
dateTimeEdit = QtWidgets.QDateTimeEdit(datetime.datetime.today())
button = QtWidgets.QPushButton("Сделать текущей секцию с годом")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(dateTimeEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
dateTimeEdit.setSelectedSection(QtWidgets.QDateTimeEdit.Section.YearSection)
sys.exit(app.exec())
