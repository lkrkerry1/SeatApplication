from display.widgets import *
from utils import constants as cs
from PyQt5 import QtWidgets

import os, time


class Ui_HistoryWindow(MyWindow):  # TODO: OOP
    def __init__(self):
        super().__init__()
        self.setupUi("history")

        self.glut = QtWidgets.QGridLayout()
        self.main.setLayout(self.glut)

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
            self.glut.addWidget(n, 1, i)

        for i, file in enumerate(files):  # Make an index column

            data = QtWidgets.QLabel(file)
            data.setFont(QtGui.QFont("宋体", 32, QtGui.QFont.Black))
            self.glut.addWidget(data, i + 2, 0)

            buttons = QtWidgets.QWidget()
            button_glut = QtWidgets.QHBoxLayout()
            buttons.setLayout(button_glut)
            self.glut.addWidget(buttons, i + 2, 1, QtCore.Qt.AlignLeft)

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
            button_glut.addWidget(open_button, 1)
            del_button = ClickableLabel(self.main)
            del_button.setObjectName("del_button")
            del_button.setFixedSize(60, 60)
            del_button.setStyleSheet(
                "#del_button{border-image:url($MAIN)}".replace(
                    "$MAIN", cs.DEL_BUTTON.replace("\\", "/")
                )
            )
            button_glut.addWidget(del_button, 2)
