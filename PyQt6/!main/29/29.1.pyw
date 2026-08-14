from PyQt6 import QtCore, QtWidgets, QtMultimedia
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                         flags=QtCore.Qt.WindowType.Window |
                               QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Аудиопроигрыватель")
        # Создаем устройство вывода звука
        self.aOutput = QtMultimedia.QAudioOutput(parent=self)
        self.aOutput.setVolume(0.5)
        # Создаем сам проигрыватель
        self.mplPlayer = QtMultimedia.QMediaPlayer(parent=self)
        self.mplPlayer.setAudioOutput(self.aOutput)
        self.mplPlayer.mediaStatusChanged.connect(self.initPlayer)
        self.mplPlayer.playbackStateChanged.connect(self.setPlayerState)
        vbox = QtWidgets.QVBoxLayout()
        # Создаем кнопку открытия файла
        btnOpen = QtWidgets.QPushButton("&Открыть файл...")
        btnOpen.clicked.connect(self.openFile)
        vbox.addWidget(btnOpen)
        # Создаем компоненты для управления воспроизведением.
        # Делаем их изначально недоступными
        self.sldPosition = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.sldPosition.setMinimum(0)
        self.sldPosition.valueChanged.connect(self.mplPlayer.setPosition)
        self.mplPlayer.positionChanged.connect(self.sldPosition.setValue)
        self.sldPosition.setEnabled(False)
        vbox.addWidget(self.sldPosition)
        hbox = QtWidgets.QHBoxLayout()
        self.btnPlay = QtWidgets.QPushButton("&Пуск")
        self.btnPlay.clicked.connect(self.mplPlayer.play)
        self.btnPlay.setEnabled(False)
        hbox.addWidget(self.btnPlay)
        self.btnPause = QtWidgets.QPushButton("П&ауза")
        self.btnPause.clicked.connect(self.mplPlayer.pause)
        self.btnPause.setEnabled(False)
        hbox.addWidget(self.btnPause)
        self.btnStop = QtWidgets.QPushButton("&Стоп")
        self.btnStop.clicked.connect(self.mplPlayer.stop)
        self.btnStop.setEnabled(False)
        hbox.addWidget(self.btnStop)
        vbox.addLayout(hbox)
        # Создаем компоненты для управления громкостью
        hbox = QtWidgets.QHBoxLayout()
        lblVolume = QtWidgets.QLabel("&Громкость")
        hbox.addWidget(lblVolume)
        self.sldVolume = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.sldVolume.setRange(0, 100)
        self.sldVolume.setTickPosition(
                          QtWidgets.QSlider.TickPosition.TicksAbove)
        self.sldVolume.setTickInterval(10)
        self.sldVolume.setValue(50)
        lblVolume.setBuddy(self.sldVolume)
        self.sldVolume.valueChanged.connect(self.setVolume)
        hbox.addWidget(self.sldVolume)
        btnMute = QtWidgets.QPushButton("&Тихо!")
        btnMute.setCheckable(True)
        btnMute.toggled.connect(self.aOutput.setMuted)
        hbox.addWidget(btnMute)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.resize(300, 100)

    # Для открытия файла используем метод getOpenFileUrl() класса
    # QFileDialog, т. к. для указания источника у проигрывателя
    # нам нужен путь к файлу, заданный в виде объекта класса QUrl
    def openFile(self):
        file = QtWidgets.QFileDialog.getOpenFileUrl(parent=self,
                         caption="Выберите звуковой файл",
                         filter="Звуковые файлы (*.mp3 *.ac3)")
        if file[1]:
            self.mplPlayer.setSource(file[0])

    def initPlayer(self, state):
        match state:
            case QtMultimedia.QMediaPlayer.MediaStatus.LoadedMedia:
                # После загрузки файла подготавливаем проигрыватель
                # для его воспроизведения
                self.mplPlayer.stop()
                self.btnPlay.setEnabled(True)
                self.btnPause.setEnabled(False)
                self.sldPosition.setEnabled(True)
                self.sldPosition.setMaximum(self.mplPlayer.duration())
            case QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia:
                # По окончании воспроизведения файла возвращаем
                # проигрыватель в изначальное состояние
                self.mplPlayer.stop()
                self.sldPosition.setValue(0)
                self.sldPosition.setEnabled(False)
                self.btnPlay.setEnabled(False)
                self.btnPause.setEnabled(False)
                self.btnStop.setEnabled(False)
            case QtMultimedia.QMediaPlayer.MediaStatus.NoMedia | \
                 QtMultimedia.QMediaPlayer.MediaStatus.InvalidMedia:
                # Если файл не был загружен, отключаем компоненты,
                # управляющие воспроизведением
                self.sldPosition.setValue(0)
                self.sldPosition.setEnabled(False)
                self.btnPlay.setEnabled(False)
                self.btnPause.setEnabled(False)
                self.btnStop.setEnabled(False)

    # В зависимости от того, воспроизводится ли файл, поставлен
    # ли он на паузу или остановлен, делаем соответствующие кнопки
    # доступными или недоступными
    def setPlayerState(self, state):
        match state:
            case QtMultimedia.QMediaPlayer.PlaybackState.StoppedState:
                self.sldPosition.setValue(0)
                self.btnPlay.setEnabled(True)
                self.btnPause.setEnabled(False)
                self.btnStop.setEnabled(False)
            case QtMultimedia.QMediaPlayer.PlaybackState.PlayingState:
                self.btnPlay.setEnabled(False)
                self.btnPause.setEnabled(True)
                self.btnStop.setEnabled(True)
            case QtMultimedia.QMediaPlayer.PlaybackState.PausedState:
                self.btnPlay.setEnabled(True)
                self.btnPause.setEnabled(False)
                self.btnStop.setEnabled(True)

    def setVolume(self, value):
        self.aOutput.setVolume(value / 100)

    # При закрытии окна останавливаем воспроизведение
    def closeEvent(self, e):
        self.mplPlayer.stop()
        e.accept()
        QtWidgets.QWidget.closeEvent(self, e)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
