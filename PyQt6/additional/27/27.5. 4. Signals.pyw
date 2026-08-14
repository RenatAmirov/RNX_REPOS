from PyQt6 import QtCore, QtWidgets
import sys

def on_current_changed(s):
    print("on_current_changed", s)

def on_directory_entered(s):
    print("on_directory_entered", s)

def on_file_selected(s):
    print("on_file_selected", s)

def on_files_selected(s):
    print("on_files_selected", s)

def on_filter_selected(s):
    print("on_filter_selected", s)

def on_clicked():
    dialog = QtWidgets.QFileDialog(parent=window,
                        filter="All (*);;Images (*.png *.jpg)",
                        caption="Это заголовок окна")
    dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptOpen)
    dialog.setDirectory(QtCore.QDir.currentPath())
    dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)
    dialog.setSidebarUrls([QtCore.QUrl.fromLocalFile("C:\\work"),
                           QtCore.QUrl.fromLocalFile("C:\\work\\!temp")])
    dialog.currentChanged[str].connect(on_current_changed)
    dialog.directoryEntered[str].connect(on_directory_entered)
    dialog.fileSelected[str].connect(on_file_selected)
    dialog.filesSelected["QStringList"].connect(on_files_selected)
    dialog.filterSelected[str].connect(on_filter_selected)

    result = dialog.exec()
    if result == QtWidgets.QDialog.DialogCode.Accepted:
        print(dialog.selectedFiles())
    else:
        print("Нажата кнопка Cancel")

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QFileDialog")
window.resize(300, 70)

button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window.setLayout(box)
window.show()

sys.exit(app.exec())
