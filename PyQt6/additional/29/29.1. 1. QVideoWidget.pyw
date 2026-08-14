from PyQt6 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent,
                                   flags=QtCore.Qt.WindowType.Window)
        self.setWindowTitle("Видеопроигрыватель")
        self.aOutput = QtMultimedia.QAudioOutput(parent=self)
        self.aOutput.setVolume(0.5)
        self.mplPlayer = QtMultimedia.QMediaPlayer()
        self.mplPlayer.setAudioOutput(self.aOutput)
        self.mplPlayer.mediaStatusChanged.connect(self.initPlayer)
        self.mplPlayer.playbackStateChanged.connect(self.setPlayerState)
        vbox = QtWidgets.QVBoxLayout()
        btnOpen = QtWidgets.QPushButton("&Открыть файл...")
        btnOpen.clicked.connect(self.openFile)
        vbox.addWidget(btnOpen)
        vwg = QtMultimediaWidgets.QVideoWidget()
        vwg.setAspectRatioMode(QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.mplPlayer.setVideoOutput(vwg)
        vbox.addWidget(vwg)
        self.sldPosition = QtWidgets.QSlider(
                             QtCore.Qt.Orientation.Horizontal)
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
        hbox = QtWidgets.QHBoxLayout()
        lblVolume = QtWidgets.QLabel("&Громкость")
        hbox.addWidget(lblVolume)
        sldVolume = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        sldVolume.setRange(0, 100)
        sldVolume.setTickPosition(
                     QtWidgets.QSlider.TickPosition.TicksAbove)
        sldVolume.setTickInterval(10)
        sldVolume.setValue(50)
        lblVolume.setBuddy(sldVolume)
        sldVolume.valueChanged.connect(self.setVolume)
        hbox.addWidget(sldVolume)
        btnMute = QtWidgets.QPushButton("&Тихо!")
        btnMute.setCheckable(True)
        btnMute.toggled.connect(self.aOutput.setMuted)
        hbox.addWidget(btnMute)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.resize(300, 300)

    def openFile(self):
        file = QtWidgets.QFileDialog.getOpenFileUrl(parent=self,
                              caption="Выберите видеофайл",
                              filter="Видеофайлы (*.avi *.mp4)")
        if file[1]:
            self.mplPlayer.setSource(file[0])

    def initPlayer(self, state):
        match state:
            case QtMultimedia.QMediaPlayer.MediaStatus.LoadedMedia:
                self.mplPlayer.stop()
                self.btnPlay.setEnabled(True)
                self.btnPause.setEnabled(False)
                self.sldPosition.setEnabled(True)
                self.sldPosition.setMaximum(self.mplPlayer.duration())
            case QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia:
                self.mplPlayer.stop()
                self.sldPosition.setValue(0)
                self.sldPosition.setEnabled(False)
                self.btnPlay.setEnabled(False)
                self.btnPause.setEnabled(False)
                self.btnStop.setEnabled(False)
            case QtMultimedia.QMediaPlayer.MediaStatus.NoMedia | \
                 QtMultimedia.QMediaPlayer.MediaStatus.InvalidMedia:
                self.sldPosition.setValue(0)
                self.sldPosition.setEnabled(False)
                self.btnPlay.setEnabled(False)
                self.btnPause.setEnabled(False)
                self.btnStop.setEnabled(False)

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

    def closeEvent(self, e):
        self.mplPlayer.stop()
        e.accept()
        QtWidgets.QWidget.closeEvent(self, e)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
