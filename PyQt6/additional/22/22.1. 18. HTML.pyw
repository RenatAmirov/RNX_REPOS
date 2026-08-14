from PyQt6 import QtCore, QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
label = QtWidgets.QLabel()
label.setWindowTitle("Класс QLabel")
label.resize(500, 150)
label.setText("""
<style type="text/css">
p { background-color: white; }
</style>
<h1 align="center">Заголовок первого уровня</h1>
<p style="margin: 0 10px 0 10px;">Текст абзаца 
<b>полужирный</b>, <i>курсивный</i>, 
<span style="color: red;">выделенный красным</span><br><br>
<center><a href="http://google.ru/">Это гиперссылка</a></center>
</p>
""")
label.show()
sys.exit(app.exec())
