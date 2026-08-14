from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QProgressBar")
window.resize(300, 70)
progressBar = QtWidgets.QProgressBar()
progressBar.setRange(0, 0)
box = QtWidgets.QVBoxLayout()
box.addWidget(progressBar)
window.setLayout(box)
window.show()
sys.exit(app.exec())
