from PyQt6 import QtCore, QtWidgets
import sys

def on_link_activated(link):
    print(link)

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QLabel")
window.resize(300, 150)
label = QtWidgets.QLabel()
label.setText("""<a href="https://www.google.ru/">Это гиперссылка 1</a>
<a href="https://bhv.ru/">Это гиперссылка 2</a>
""")
label.setFrameStyle(QtWidgets.QFrame.Shape.Box |
                    QtWidgets.QFrame.Shadow.Plain)
label.setTextInteractionFlags(
         QtCore.Qt.TextInteractionFlag.LinksAccessibleByKeyboard)
label.linkActivated[str].connect(on_link_activated)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
window.setLayout(vbox)
window.show()
sys.exit(app.exec())
