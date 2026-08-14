from PyQt6 import QtWidgets
import sys

def on_clicked():
    print(comboBox.currentFont().family())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QFontComboBox")
window.resize(500, 90)
comboBox = QtWidgets.QFontComboBox()
comboBox.setFontFilters(QtWidgets.QFontComboBox.FontFilter.MonospacedFonts)
button = QtWidgets.QPushButton("Получить значение")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(comboBox)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
