from display.widgets import *
from utils import constants as cst
from utils.io import SeatingTable

import os
import PyQt5
import PyQt5.QtMultimediaWidgets
from PyQt5 import QtWidgets, QtMultimedia, QtCore, QtGui


class Ui_StartWindow(MyWindow):
    def __init__(self):
        super().__init__()
        self.setupUi("start")

        # Play the vedio
        self.media_player = QtMultimedia.QMediaPlayer(
            None, QtMultimedia.QMediaPlayer.VideoSurface
        )
        self.video_widget = PyQt5.QtMultimediaWidgets.QVideoWidget(self.main)
        self.video_widget.setGeometry(0, 0, 1600, 900)
        self.media_player.setVideoOutput(self.video_widget)
        if cst.DEBUG:
            print("opening {}".format(cst.RANDOMIZE_VEDIO).replace("\\", "/"))
        self.media = QtMultimedia.QMediaContent(
            QtCore.QUrl.fromLocalFile(cst.RANDOMIZE_VEDIO.replace("\\", "/"))
        )
        self.media_player.setMedia(self.media)
        self.video_widget.lower()

        self.skip_button = ClickableLabel(self.main)
        self.skip_button.setGeometry(1570, 0, 1600, 30)
        self.skip_button.clicked.connect(self.skip)

        # Display the table
        self.table = QtWidgets.QTableWidget(self.main)
        self.table.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )
        self.table.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch
        )  # Fill all the space
        self.table.setGeometry(0, 0, 1600, 900)
        self.table.verticalHeader().setVisible(False)  # Hide the first column
        self.table.horizontalHeader().setVisible(False)  # Hide the first row
        self.media_player.mediaStatusChanged.connect(self.finish)
        self.table.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers
        )  # TODO: Change into can edit and add a save button

    def show(self):
        self.main.show()
        self.table.hide()
        self.back.hide()
        self.video_widget.show()
        self.media_player.play()

    def close(self):
        self.media_player.pause()
        self.media_player.stop()
        self.main.close()

    def skip(self):
        self.media_player.pause()
        self.media_player.stop()
        self.table.show()
        self.back.show()
        self.video_widget.hide()
        self.table.lower()

    def finish(self):
        if (
            self.media_player.mediaStatus() == QtMultimedia.QMediaPlayer.EndOfMedia
        ):  # The vedio has ended
            self.table.show()
            self.back.show()
            self.video_widget.hide()
            self.table.lower()

    def display(self, seating: SeatingTable):
        self.col = seating.table_num["GroupNum"] * seating.table_num["LineOfGroup"]
        self.row = max(*seating.table_num["ColumnOfGroup"])
        self.table.setColumnCount(self.col)
        self.table.setRowCount(self.row + 1)
        for i in range(self.col):  # Make an index column
            data = QtWidgets.QTableWidgetItem(
                str(i // seating.table_num["LineOfGroup"] + 1)
            )
            data.setFont(QtGui.QFont("宋体", 64, QtGui.QFont.Black))
            data.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(
                0,
                i,
                data,
            )
        for i in range(self.col):
            for j in range(
                seating.table_num["ColumnOfGroup"][
                    i // seating.table_num["LineOfGroup"]
                ]
            ):
                data = QtWidgets.QTableWidgetItem(
                    seating.table[i // seating.table_num["LineOfGroup"]][j][
                        i % seating.table_num["LineOfGroup"]
                    ]
                )
                data.setFont(QtGui.QFont("宋体", 64, QtGui.QFont.Black))
                data.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(
                    j + 1,
                    i,
                    data,
                )
        for i in range(seating.table_num["GroupNum"]):
            self.table.setSpan(0, i * 2, 1, seating.table_num["LineOfGroup"])
