from display.widgets import *
from PyQt5 import QtWidgets


class Ui_SettingsWindow(MyWindow):
    def __init__(self):
        super().__init__()
        self.setupUi("settings")

    def show(self):
        self.main.show()

    def close(self):
        self.main.close()
