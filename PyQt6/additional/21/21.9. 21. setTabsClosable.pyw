from PyQt6 import QtWidgets
import sys

def on_tab_close(index):
    print("on_tab_close", index)

def on_current_changed(index):
    print("on_current_changed", index)
    
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QTabWidget")
window.resize(400, 350)
tab = QtWidgets.QTabWidget()
tab.currentChanged["int"].connect(on_current_changed)
tab.tabCloseRequested["int"].connect(on_tab_close)
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 1"), "Вкладка &1")
tab.addTab(QtWidgets.QLabel("Содержимое вкладки 2"), "Вкладка &2")
tab.setTabsClosable(True)
tab.setCurrentIndex(0)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(tab)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
