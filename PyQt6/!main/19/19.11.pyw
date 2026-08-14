from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget(flags=QtCore.Qt.WindowType.Dialog |
                           QtCore.Qt.WindowType.WindowContextHelpButtonHint)
window.setWindowTitle("Всплывающие и расширенные подсказки")
window.resize(300, 70)
button = QtWidgets.QPushButton("Закрыть окно", window)
button.setFixedSize(150, 30)
button.move(75, 20)
button.setToolTip("Это всплывающая подсказка для кнопки")
button.setToolTipDuration(3000)
window.setToolTip("Это всплывающая подсказка для окна")
button.setToolTipDuration(5000)
button.setWhatsThis("Это расширенная подсказка для кнопки")
window.setWhatsThis("Это расширенная подсказка для окна")
button.clicked.connect(QtWidgets.QApplication.instance().quit)
window.show()
sys.exit(app.exec())
