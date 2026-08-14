from PyQt6 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
import sys, os

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                  flags=QtCore.Qt.WindowType.Window |
                        QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Запись видео")
        # Создаем транспорт, звуковой вход, камеру и кодировщик
        mcs = QtMultimedia.QMediaCaptureSession(parent=self)
        self.aInput = QtMultimedia.QAudioInput(parent=self)
        self.aInput.setVolume(1.0)
        mcs.setAudioInput(self.aInput)
        cam = QtMultimedia.QCamera(parent=self)
        mcs.setCamera(cam)
        self.ardRecorder = QtMultimedia.QMediaRecorder(parent=self)
        mcs.setRecorder(self.ardRecorder)
        # Запускаем захват видео созданной ранее камерой
        cam.start()
        # Видео будет сохраняться в файле movie.mp4, находящемся
        # в той же папке, где хранится программа
        fn = QtCore.QUrl.fromLocalFile(os.path.abspath("movie.mp4"))
        self.ardRecorder.setOutputLocation(fn)
        mf = QtMultimedia.QMediaFormat(
                          QtMultimedia.QMediaFormat.FileFormat.MPEG4)
        mf.setAudioCodec(QtMultimedia.QMediaFormat.AudioCodec.AAC)
        mf.setVideoCodec(QtMultimedia.QMediaFormat.VideoCodec.H264)
        self.ardRecorder.setMediaFormat(mf)
        # Задаем параметры кодирования звука и видео
        self.ardRecorder.setQuality(
                QtMultimedia.QMediaRecorder.Quality.LowQuality)
        self.ardRecorder.setEncodingMode(
            QtMultimedia.QMediaRecorder.EncodingMode.ConstantQualityEncoding)
        self.ardRecorder.setAudioChannelCount(1)
        self.ardRecorder.setAudioSampleRate(-1)
        self.ardRecorder.setVideoResolution(QtCore.QSize())
        self.ardRecorder.recorderStateChanged.connect(self.initRecorder)
        self.ardRecorder.durationChanged.connect(self.showDuration)
        vbox = QtWidgets.QVBoxLayout()
        # Создаем контрольную видеопанель и связываем ее с транспортом
        vwg = QtMultimediaWidgets.QVideoWidget()
        vwg.setAspectRatioMode(QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        mcs.setVideoOutput(vwg)
        vbox.addWidget(vwg, stretch=1)
        # Создаем компоненты для запуска, приостановки и остановки
        # записи видео
        hbox = QtWidgets.QHBoxLayout()
        self.btnRecord = QtWidgets.QPushButton("&Запись")
        self.btnRecord.clicked.connect(self.ardRecorder.record)
        hbox.addWidget(self.btnRecord)
        self.btnPause = QtWidgets.QPushButton("П&ауза")
        self.btnPause.clicked.connect(self.ardRecorder.pause)
        self.btnPause.setEnabled(False)
        hbox.addWidget(self.btnPause)
        self.btnStop = QtWidgets.QPushButton("&Стоп")
        self.btnStop.clicked.connect(self.ardRecorder.stop)
        self.btnStop.setEnabled(False)
        hbox.addWidget(self.btnStop)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox)
        # Создаем надпись, в которую будет выводиться состояние программы
        self.lblStatus = QtWidgets.QLabel("Готово")
        vbox.addWidget(self.lblStatus)
        self.setLayout(vbox)
        self.resize(300, 280)

    # В зависимости от состояния записи видео делаем нужные
    # кнопки доступными или, напротив, недоступными и выводим
    # соответствующий текст в надписи
    def initRecorder(self, state):
        match state:
            case QtMultimedia.QMediaRecorder.RecorderState.RecordingState:
                self.btnRecord.setEnabled(False)
                self.btnPause.setEnabled(True)
                self.btnStop.setEnabled(True)
                self.lblStatus.setText("Запись")
            case QtMultimedia.QMediaRecorder.RecorderState.PausedState:
                self.btnRecord.setEnabled(True)
                self.btnPause.setEnabled(False)
                self.lblStatus.setText("Пауза")
            case QtMultimedia.QMediaRecorder.RecorderState.StoppedState:
                self.btnRecord.setEnabled(True)
                self.btnPause.setEnabled(False)
                self.btnStop.setEnabled(False)
                self.lblStatus.setText("Готово")

    # Выводим продолжительность записанного видео
    def showDuration(self, duration):
        self.lblStatus.setText("Записано " + str(duration // 1000) +
                               " секунд")

    # При закрытии окна останавливаем запись
    def closeEvent(self, e):
        self.ardRecorder.stop()
        e.accept()
        QtWidgets.QWidget.closeEvent(self, e)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
