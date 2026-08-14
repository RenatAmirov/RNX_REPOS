from PyQt6 import QtWidgets, QtCore
import sys, time

def on_clicked():
    button.setDisabled(True)            # Делаем кнопку неактивной
    for i in range(1, 21):
        # Обрабатываем накопившиеся события всех типов в течение 1 с
        QtWidgets.QApplication.instance().processEvents(
                  QtCore.QEventLoop.ProcessEventsFlag.AllEvents, 1000)
        time.sleep(1)                   # «Засыпаем» на 1 секунду
        print("step -", i)
    button.setDisabled(False)           # Делаем кнопку активной

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Запустить процесс")
button.resize(200, 40)
button.clicked.connect(on_clicked)
button.show()
sys.exit(app.exec())
