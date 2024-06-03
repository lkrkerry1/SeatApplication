from display.widgets import *
from PyQt5 import QtWidgets

import os


class Ui_HistoryWindow:
    def __init__(self):
        self.main = QtWidgets.QMainWindow()
        self.main.resize(1600, 900)
        self.main.resize(1600, 900)
        self.main.setObjectName("history")
        self.back = ClickableLabel(self.main)
        self.back.setGeometry(0, 0, 80, 80)

        self.table = QtWidgets.QTableWidget(self.main)
        self.table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )
        self.table.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )  # Fill all the space
        self.table.setGeometry(0, 0, 1600, 900)
        self.table.verticalHeader().setVisible(False)  # Hide the first column
        self.table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers
        )  # TODO: Change into can edit and add a save button

        self.back.setGeometry(0, 0, 80, 80)

    def show(self):
        self.main.show()

    def close(self):
        self.main.close()

        self.display(["a", "b", "c"])

    def display(self, files):
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["文件", "性别", "体重（kg）"])
        self.table.setRowCount(len(files))
        for i, file in enumerate(files):  # Make an index column
            data = QtWidgets.QTableWidgetItem(file)
            data.setFont(QtGui.QFont("宋体", 64, QtGui.QFont.Black))
            data.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(
                i,
                0,
                data,
            )
