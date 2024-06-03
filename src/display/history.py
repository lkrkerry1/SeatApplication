from display.widgets import *
from utils import constants as cs
from PyQt5 import QtWidgets

import os, time


class Ui_HistoryWindow:  # TODO: OOP
    def __init__(self):
        self.main = QtWidgets.QWidget()
        self.main.resize(1600, 900)
        self.main.setObjectName("history")
        self.back = ClickableLabel(self.main)
        self.back.setGeometry(0, 0, 80, 80)

        self.layout = QtWidgets.QGridLayout()
        self.main.setLayout(self.layout)
        self.layout.addWidget(self.back, 0, 0)

    def show(self):
        self.main.show()
        files = os.listdir(cs.OUTPUT_DIR)
        result = []
        for file in files:
            if file.endswith(".dat"):
                name = file[:-4]
                time_array = time.localtime(float(name))
                file = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
                result.append(file)
        while len(result) <= cs.BUFFER_SIZE:
            result.append("")
        if cs.DEBUG:
            print("History files: {}".format(result))
        self.display(result)

    def close(self):
        self.main.close()

    def display(self, files):
        # nav
        self.nav = [QtWidgets.QLabel("文件"), QtWidgets.QLabel("操作")]
        for i, n in enumerate(self.nav):
            n.setFont(QtGui.QFont("宋体", 32, QtGui.QFont.Black))
            self.layout.addWidget(n, 1, i)

        for i, file in enumerate(files):  # Make an index column

            data = QtWidgets.QLabel(file)
            data.setFont(QtGui.QFont("宋体", 32, QtGui.QFont.Black))
            self.layout.addWidget(data, i + 2, 0)

            buttons = QtWidgets.QWidget()
            button_layout = QtWidgets.QHBoxLayout()
            buttons.setLayout(button_layout)
            self.layout.addWidget(buttons, i + 2, 1, QtCore.Qt.AlignLeft)

            if file == "":
                continue

            open_button = ClickableLabel(self.main)
            open_button.setObjectName("open_button")
            open_button.setFixedSize(60, 60)
            open_button.setStyleSheet(
                "#open_button{border-image:url($MAIN)}".replace(
                    "$MAIN", cs.OPEN_BUTTON.replace("\\", "/")
                )
            )
            button_layout.addWidget(open_button, 1)
            del_button = ClickableLabel(self.main)
            del_button.setObjectName("del_button")
            del_button.setFixedSize(60, 60)
            del_button.setStyleSheet(
                "#del_button{border-image:url($MAIN)}".replace(
                    "$MAIN", cs.DEL_BUTTON.replace("\\", "/")
                )
            )
            button_layout.addWidget(del_button, 2)
