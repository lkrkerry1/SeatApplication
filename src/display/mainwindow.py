import os
from display.widgets import *
from utils import constants as cst

from PyQt5 import QtWidgets


class Ui_MainWindow:
    def __init__(self):
        self.main = QtWidgets.QMainWindow()
        self.main.resize(1600, 900)
        self.main.setObjectName("main")
        if cst.DEBUG:
            print("current dir {}".format(os.getcwd()))
            print("opening {}".format(cst.BACKGROUND_PICTURE.replace("\\", "/")))
        self.main.setStyleSheet(
            "#main{border-image:url($MAIN)}".replace(
                "$MAIN", cst.BACKGROUND_PICTURE.replace("\\", "/")
            )
        )

        self.start_lab = ClickableLabel(self.main)
        self.start_lab.setObjectName("startlab")
        self.start_lab.setStyleSheet("#startlab{background-color: transparent;}")
        self.start_lab.setGeometry(46, 304, 225, 103)

        self.history_lab = ClickableLabel(self.main)
        self.history_lab.setObjectName("historylab")
        self.history_lab.setStyleSheet("#historylab{background-color: transparent;}")
        self.history_lab.setGeometry(46, 437, 225, 103)

        self.settings_lab = ClickableLabel(self.main)
        self.settings_lab.setObjectName("settingslab")
        self.settings_lab.setStyleSheet("#settingslab{background-color: transparent;}")
        self.settings_lab.setGeometry(46, 570, 225, 103)

        self.exit_lab = ClickableLabel(self.main)
        self.exit_lab.setObjectName("exitlab")
        self.exit_lab.setStyleSheet("#exitlab{background-color: transparent;}")
        self.exit_lab.setGeometry(46, 703, 225, 103)

    def show(self):
        self.main.show()
