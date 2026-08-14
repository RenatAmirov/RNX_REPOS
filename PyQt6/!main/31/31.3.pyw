from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
settings = QtCore.QSettings("Прохоренок и Дронов", "Тест 2")
l = ["Python", "Ruby", "PHP", "JavaScript"]
print(l)
print("Сохраняем список")
settings.beginWriteArray("Список")
for i, el in enumerate(l):
    settings.setArrayIndex(i)
    settings.setValue("Элемент", el)
settings.endArray()
settings.sync()
print("Считываем список")
ll = []
lSize = settings.beginReadArray("Список")
for i in range(lSize):
    settings.setArrayIndex(i)
    ll.append(settings.value("Элемент"))
settings.endArray()
print(ll)
settings.clear()
