from PyQt6 import QtWidgets
import sys, datetime

def section_to_str(section):
    match section:
        case QtWidgets.QDateTimeEdit.Section.DaySection:
            return "День"
        case QtWidgets.QDateTimeEdit.Section.MonthSection:
            return "Месяц"
        case QtWidgets.QDateTimeEdit.Section.YearSection:
            return "Год"
        case QtWidgets.QDateTimeEdit.Section.HourSection:
            return "Часы"
        case QtWidgets.QDateTimeEdit.Section.MinuteSection:
            return "Минуты"
        case QtWidgets.QDateTimeEdit.Section.SecondSection:
            return "Секунды"
    return ""

def on_clicked():
    print("Всего секций -", dateTimeEdit.sectionCount())
    print("currentSectionIndex() -", dateTimeEdit.currentSectionIndex())
    print("currentSection() -", section_to_str(dateTimeEdit.currentSection()))
    print("sectionAt(1) -", section_to_str(dateTimeEdit.sectionAt(1)))
    print("День -", dateTimeEdit.sectionText(
                                 QtWidgets.QDateTimeEdit.Section.DaySection))

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QDateTimeEdit")
window.resize(300, 70)
dateTimeEdit = QtWidgets.QDateTimeEdit(datetime.datetime.today())
button = QtWidgets.QPushButton("Вывести значения")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(dateTimeEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
dateTimeEdit.setSelectedSection(QtWidgets.QDateTimeEdit.Section.YearSection)
sys.exit(app.exec())
