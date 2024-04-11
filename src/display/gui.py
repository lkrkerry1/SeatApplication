from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import Qt
import sys
from display.mainwindow import Ui_MainWindow

class GUI:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.mainwindow = Ui_MainWindow()
    def start(self):
        self.mainwindow.show()
        sys.exit(self.app.exec_())