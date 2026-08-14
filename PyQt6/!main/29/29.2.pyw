from PyQt6 import QtCore, QtWidgets, QtMultimedia
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent,
                  flags=QtCore.Qt.WindowType.Window |
                        QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle("Метаданные")
        self.mplPlayer = QtMultimedia.QMediaPlayer(self)
        self.mplPlayer.metaDataChanged.connect(self.showMetadata)
        vbox = QtWidgets.QVBoxLayout()
        btnOpen = QtWidgets.QPushButton("&Открыть файл...")
        btnOpen.clicked.connect(self.openFile)
        vbox.addWidget(btnOpen)
        # Создаем доступную только для чтения область редактирования,
        # в которую будет выводиться результат
        self.txtOutput = QtWidgets.QTextEdit()
        self.txtOutput.setReadOnly(True)
        vbox.addWidget(self.txtOutput)
        self.setLayout(vbox)
        self.resize(300, 250)

    def openFile(self):
        file = QtWidgets.QFileDialog.getOpenFileUrl(parent=self,
                         caption="Выберите звуковой файл",
                         filter="Звуковые файлы (*.mp3 *.ac3)")
        if file[1]:
            self.mplPlayer.setSource(file[0])

    def showMetadata(self):
        # Как только метаданные будут получены…
        # …очищаем область редактирования…
        self.txtOutput.clear()
        # …извлекаем объект с метаданными…
        md = self.mplPlayer.metaData()
        s = ""
        # …перебираем их в цикле…
        for k in list(QtMultimedia.QMediaMetaData.Key):
            v = md.value(k)
            # …проверяем, действительно ли существует значение
            # с таким ключом…
            if v:
                # …если значение представляет собой список,
                # преобразуем его в строку…
                if v is list:
                    v = ", ".join(v)
                # …формируем на основе значений текст…
                s += "<strong>" + k.name + "</strong>: " + str(v) + "<br>"
        # …и выводим его в область редактирования
        self.txtOutput.setHtml(s)

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
