from PyQt6 import QtCore, QtWidgets
import sys

def on_anchor_clicked(url):
    print("on_anchor_clicked", url)

def on_backward_available(status):
    print("on_backward_available", status)
    
def on_forward_available(status):
    print("on_forward_available", status)

def on_highlighted1(url):
    print("on_highlighted1", url)

def on_highlighted2(s):
    print("on_highlighted2", s)

def on_history_changed():
    print("on_history_changed")

def on_source_changed(url):
    print("on_source_changed", url)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTextBrowser")
window.resize(320, 240)
textBrowser = QtWidgets.QTextBrowser()
textBrowser.anchorClicked.connect(on_anchor_clicked)
textBrowser.backwardAvailable["bool"].connect(on_backward_available)
textBrowser.forwardAvailable["bool"].connect(on_forward_available)
textBrowser.highlighted.connect(on_highlighted1)
textBrowser.highlighted.connect(on_highlighted2)
textBrowser.historyChanged.connect(on_history_changed)
textBrowser.sourceChanged.connect(on_source_changed)
textBrowser.setSource(QtCore.QUrl("test.html"))
button = QtWidgets.QPushButton("Очистить список истории")
button.clicked.connect(textBrowser.clearHistory)
button2 = QtWidgets.QPushButton("Назад")
button2.clicked.connect(textBrowser.backward)
button3 = QtWidgets.QPushButton("Вперед")
button3.clicked.connect(textBrowser.forward)
box = QtWidgets.QVBoxLayout()
box.addWidget(textBrowser)
box.addWidget(button)
box.addWidget(button2)
box.addWidget(button3)
window.setLayout(box)
window.show()
sys.exit(app.exec())
