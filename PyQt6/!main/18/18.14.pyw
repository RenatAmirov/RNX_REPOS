from PyQt6 import QtCore, QtWidgets

class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False   # Флаг выполнения
        self.count = 0
    def run(self):
        self.running = True
        while self.running:    # Проверяем значение флага
            self.count += 1
            self.mysignal.emit("count = %s" % self.count)
            self.sleep(1)      # Имитируем процесс

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Нажмите кнопку для запуска потока")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.btnStart = QtWidgets.QPushButton("Запустить поток")
        self.btnStop = QtWidgets.QPushButton("Остановить поток")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnStart)
        self.vbox.addWidget(self.btnStop)
        self.setLayout(self.vbox)
        self.mythread = MyThread()
        self.btnStart.clicked.connect(self.on_start)
        self.btnStop.clicked.connect(self.on_stop)
        self.mythread.mysignal.connect(self.on_change,
                               QtCore.Qt.ConnectionType.QueuedConnection)
    def on_start(self):
        if not self.mythread.isRunning():
            self.mythread.start()      # Запускаем поток
    def on_stop(self):
        self.mythread.running = False  # Изменяем флаг выполнения
    def on_change(self, s):
        self.label.setText(s)
    def closeEvent(self, event):       # Вызывается при закрытии окна
        self.hide()                    # Скрываем окно
        self.mythread.running = False  # Изменяем флаг выполнения
        self.mythread.wait(5000)       # Даем время, чтобы закончить
        event.accept()                 # Закрываем окно

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Запуск и остановка потока")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec())
