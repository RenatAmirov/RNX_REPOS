from PyQt6 import QtCore, QtWidgets, QtMultimedia
import sys, os

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                  flags=QtCore.Qt.WindowType.Window |
                        QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Звуковые эффекты")
        # Инициализируем подсистему вывода звуковых эффектов
        self.sndEffect = QtMultimedia.QSoundEffect()
        # Задаем файл-источник
        fn = QtCore.QUrl.fromLocalFile(os.path.abspath("effect.wav"))
        self.sndEffect.setSource(fn)
        self.sndEffect.loopsRemainingChanged.connect(self.showCount)
        self.sndEffect.playingChanged.connect(self.clearCount)
        vbox = QtWidgets.QVBoxLayout()
        # Создаем кнопки для запуска воспроизведения звука
        lblPlay = QtWidgets.QLabel("Воспроизвести...")
        vbox.addWidget(lblPlay)
        btnOnce = QtWidgets.QPushButton("...&один раз")
        btnOnce.clicked.connect(self.playOnce)
        vbox.addWidget(btnOnce)
        btnTen = QtWidgets.QPushButton("...&десять раз")
        btnTen.clicked.connect(self.playTen)
        vbox.addWidget(btnTen)
        btnInfinite = QtWidgets.QPushButton(
                                "...&бесконечное количество раз")
        btnInfinite.clicked.connect(self.playInfinite)
        vbox.addWidget(btnInfinite)
        btnStop = QtWidgets.QPushButton("&Стоп")
        btnStop.clicked.connect(self.sndEffect.stop)
        vbox.addWidget(btnStop)
        self.lblStatus = QtWidgets.QLabel("")
        vbox.addWidget(self.lblStatus)
        self.setLayout(vbox)
        self.resize(300, 100)

    def playOnce(self):
        self.sndEffect.setLoopCount(1)
        self.sndEffect.play()

    def playTen(self):
        self.sndEffect.setLoopCount(10)
        self.sndEffect.play()

    def playInfinite(self):
        self.sndEffect.setLoopCount(-2)
        self.sndEffect.play()

    # Выводим количество повторений воспроизведения эффекта
    def showCount(self):
        self.lblStatus.setText("Воспроизведено " +
                               str(self.sndEffect.loopCount() -
                               self.sndEffect.loopsRemaining()) + " раз")

    # Если воспроизведение закончено, очищаем выведенное ранее
    # количество повторений эффекта
    def clearCount(self):
        if not self.sndEffect.isPlaying():
            self.lblStatus.setText("")

    def closeEvent(self, e):
        self.sndEffect.stop()
        e.accept()
        QtWidgets.QWidget.closeEvent(self, e)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
