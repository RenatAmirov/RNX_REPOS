from PyQt6 import QtCore, QtWidgets
import sys

class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(int)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
    def run(self):
        for i in range(1, 26):
            self.sleep(1)
            self.mysignal.emit(i * 4)

def on_clicked():
    thread.start()
    button.setEnabled(False)
    
def on_finished():
    button.setEnabled(True)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QProgressBar")
window.resize(300, 70)
progressBar = QtWidgets.QProgressBar()
progressBar.setMinimum(0)
progressBar.setMaximum(100)
thread = MyThread()
thread.finished.connect(on_finished)
thread.mysignal[int].connect(progressBar.setValue)
button = QtWidgets.QPushButton("Запустить процесс")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(progressBar)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec())
