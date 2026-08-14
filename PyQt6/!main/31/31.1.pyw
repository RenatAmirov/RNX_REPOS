from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
settings = QtCore.QSettings("Прохоренок и Дронов", "Тест 1")
v1 = 123
v2 = "Python"
v3 = QtCore.QSize(640, 480)
print(v1, v2, v3, sep=" | ")
print("Сохраняем настройки")
settings.setValue("Значение 2", v2)
settings.setValue("Значение 3", v3)
settings.sync()
print("Считываем настройки")
lv1 = settings.value("Значение 1")
lv2 = settings.value("Значение 2")
lv3 = settings.value("Значение 3")
print(lv1, lv2, lv3, sep=" | ")
if settings.contains("Значение 4"):
    print("Значение 4 в хранилище присутствует")
else:
    print("Значение 4 в хранилище отсутствует")
print("Очищаем хранилище")
settings.clear()
