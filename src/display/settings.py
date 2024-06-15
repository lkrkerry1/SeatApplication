from display.widgets import *
from utils import constants as cst

from PyQt5 import QtWidgets, QtGui


class Ui_SettingsWindow(MyWindow):
    def __init__(self):
        super().__init__()
        self.setupUi("settings")
        self.tabwidget = QtWidgets.QTabWidget(self.main)
        self.tabwidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tabwidget.setGeometry(0, cst.BUTTON_SIZE[0], 1600, 900)

        self.tabshow = QtWidgets.QWidget()
        QtWidgets.QLabel("外观内容未完成", self.tabshow).setFont(
            QtGui.QFont("宋体", 32, QtGui.QFont.Black)
        )  # TODO: finish it

        # TODO: read settings
        self.taboth = QtWidgets.QWidget()
        self.othlayout = QtWidgets.QFormLayout()
        self.othtitle1 = QtWidgets.QLabel()
        self.othtitle1.setText("人员")
        self.othtitle1.setFont(QtGui.QFont("宋体", 32, QtGui.QFont.Black))
        self.othtitle2 = QtWidgets.QLabel()
        self.othtitle2.setText("教室")
        self.othtitle2.setFont(QtGui.QFont("宋体", 32, QtGui.QFont.Black))
        self.othtitle3 = QtWidgets.QLabel()
        self.othtitle3.setText("限制")
        self.othtitle3.setFont(QtGui.QFont("宋体", 32, QtGui.QFont.Black))

        self.le1 = QtWidgets.QLineEdit()
        self.le1.setFont(QtGui.QFont("宋体", 32, QtGui.QFont.Black))
        self.le2 = QtWidgets.QLineEdit()
        self.le2.setFont(QtGui.QFont("宋体", 32, QtGui.QFont.Black))
        self.othlayout.addRow(
            self.othtitle1,
            self.le1,
        )
        self.othlayout.addRow(
            self.othtitle2,
            self.le2,
        )
        self.le3 = QtWidgets.QLineEdit()
        self.le3.setFont(QtGui.QFont("宋体", 32, QtGui.QFont.Black))
        self.othlayout.addRow(
            self.othtitle3,
            self.le3,
        )

        self.taboth.setLayout(self.othlayout)

        self.tabwidget.addTab(self.tabshow, "外观")
        self.tabwidget.addTab(self.taboth, "其他")
        self.tabwidget.setStyleSheet(
            "QTabBar::tab { height: 100px; width: 50px; font-size: 20px}"
        )

    def show(self):
        self.main.show()

    def close(self):
        self.main.close()
