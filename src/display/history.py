from display.widgets import *
from PyQt5 import QtWidgets

class Ui_HistoryWindow:
    def __init__(self):
        self.main = QtWidgets.QMainWindow()
        self.main.resize(1600,900)
        self.main.setObjectName("history")
        self.back = ClickableLabel(self.main)
        self.back.setGeometry(0,0,80,80)
    def show(self):
        self.main.show()