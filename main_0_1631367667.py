#create the Easy Editor photo editor here!
from PyQt5.QtCore import  Qt
from  PyQt5.QtWidgets import *
app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle("The Easy Editor app?")
main_win.resize(900,700)

main_win.show()
app.exec