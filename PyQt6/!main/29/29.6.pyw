from PyQt6 import QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
import sys, os

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                  flags=QtCore.Qt.WindowType.Window |
                        QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        # Создаем счетчик захваченных изображений
        self.counter = 0
        self.setWindowTitle("Захват фото")
        # Создаем транспорт, камеру и кодировщик
        mcs = QtMultimedia.QMediaCaptureSession(parent=self)
        cam = QtMultimedia.QCamera(parent=self)
        mcs.setCamera(cam)
        self.icCapture = QtMultimedia.QImageCapture(parent=self)
        mcs.setImageCapture(self.icCapture)
        cam.start()
        # Задаем параметры сохранения изображений
        self.icCapture.setFileFormat(
                       QtMultimedia.QImageCapture.FileFormat.JPEG)
        self.icCapture.setQuality(
                       QtMultimedia.QImageCapture.Quality.HighQuality)
        self.icCapture.setResolution(QtCore.QSize())
        vbox = QtWidgets.QVBoxLayout()
        # Создаем контрольную видеопанель и связываем ее с транспортом
        vwg = QtMultimediaWidgets.QVideoWidget()
        vwg.setAspectRatioMode(QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        mcs.setVideoOutput(vwg)
        vbox.addWidget(vwg, stretch=1)
        # Создаем кнопку для захвата изображения
        self.btnCapture = QtWidgets.QPushButton("&Сделать фото")
        self.btnCapture.clicked.connect(self.captureImage)
        self.icCapture.readyForCaptureChanged.connect(
                       self.btnCapture.setEnabled)
        vbox.addWidget(self.btnCapture)
        self.setLayout(vbox)
        self.resize(320, 240)

    def captureImage(self):
        self.counter += 1
        self.icCapture.captureToFile(
               os.path.abspath(str(self.counter) + ".jpg"))

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
