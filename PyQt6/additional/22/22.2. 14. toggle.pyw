from PyQt6 import QtWidgets
import sys

def on_toggled_button1(status):
    print("Кнопка переключена", status)
    
def on_clicked_button2():
    button1.toggle()
    
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QPushButton")
window.resize(300, 50)
button1 = QtWidgets.QPushButton("Кнопка")
button1.setCheckable(True)
button1.setChecked(True)
button2 = QtWidgets.QPushButton("Нажми меня")
button1.toggled["bool"].connect(on_toggled_button1)
button2.clicked.connect(on_clicked_button2)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(button1)
vbox.addWidget(button2)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
