from PyQt6 import QtCore, QtWidgets
import sys

def on_state_changed1(status):
    print("checkBox1", status)

def on_state_changed2(status):
    print("checkBox2", status)

def on_state_changed3(status):
    print("checkBox2", status)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QCheckBox")
window.resize(300, 150)
checkBox1 = QtWidgets.QCheckBox("&Unchecked")
checkBox2 = QtWidgets.QCheckBox("&PartiallyChecked")
checkBox3 = QtWidgets.QCheckBox("&Checked")
checkBox2.setTristate(True)
checkBox1.setCheckState(QtCore.Qt.CheckState.Unchecked)
checkBox2.setCheckState(QtCore.Qt.CheckState.PartiallyChecked)
checkBox3.setCheckState(QtCore.Qt.CheckState.Checked)
style = window.style()
icon1 = style.standardIcon(
              QtWidgets.QStyle.StandardPixmap.SP_DialogOkButton)
checkBox1.setIcon(icon1)
icon2 = style.standardIcon(
              QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical)
checkBox2.setIcon(icon2)
checkBox1.stateChanged["int"].connect(on_state_changed1)
checkBox1.toggled["bool"].connect(on_state_changed1)
checkBox2.stateChanged["int"].connect(on_state_changed2)
checkBox3.stateChanged["int"].connect(on_state_changed3)
box = QtWidgets.QVBoxLayout()
box.addWidget(checkBox1)
box.addWidget(checkBox2)
box.addWidget(checkBox3)
window.setLayout(box)
window.show()
sys.exit(app.exec())
