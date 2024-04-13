from PyQt5 import QtWidgets
import sys

from display.mainwindow import Ui_MainWindow
from display.start import Ui_StartWindow
from display.history import Ui_HistoryWindow
from display.settings import Ui_SettingsWindow

from utils import core


class GUI:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.mainwindow = Ui_MainWindow()
        self.startw = Ui_StartWindow()
        self.historyw = Ui_HistoryWindow()
        self.settingsw = Ui_SettingsWindow()
        self.mainwindow.start_lab.clicked.connect(lambda: self.openwindow(self.startw))
        self.mainwindow.history_lab.clicked.connect(
            lambda: self.openwindow(self.historyw)
        )
        self.mainwindow.settings_lab.clicked.connect(
            lambda: self.openwindow(self.settingsw)
        )
        self.mainwindow.exit_lab.clicked.connect(self.mainwindow.main.close)

        self.startw.back.clicked.connect(lambda: self.back(self.startw))
        self.historyw.back.clicked.connect(lambda: self.back(self.historyw))
        self.settingsw.back.clicked.connect(lambda: self.back(self.settingsw))

    def start(self):
        self.mainwindow.show()
        sys.exit(self.app.exec_())

    def openwindow(self, window):
        self.mainwindow.main.close()
        window.show()
        if window == self.startw:  # start window
            seating = core.rdesk()
            self.startw.display(seating)

    def back(self, window):
        window.close()
        self.mainwindow.main.show()
