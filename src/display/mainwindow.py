from display.widgets import *
from PyQt5 import QtWidgets

class Ui_MainWindow:
    def __init__(self):
        self.main = DraggableWindow()
        self.main=QtWidgets.QMainWindow()
        self.main.resize(1600,900)
        self.main.setObjectName("main")
        self.main.setStyleSheet("#main{border-image:url(assets/bg.png)}")
        
        self.start_lab = ClickableLabel(self.main)
        self.start_lab.setObjectName("startlab")
        self.start_lab.setStyleSheet("#startlab{background-color: transparent;}")
        self.start_lab.setGeometry(46, 304, 225, 103)
        self.start_lab.clicked.connect(lambda: print("startlab clicked")) # TODO: Put start window here
        
        self.history_lab = ClickableLabel(self.main)
        self.history_lab.setObjectName("historylab")
        self.history_lab.setStyleSheet("#historylab{background-color: transparent;}")
        self.history_lab.setGeometry(46, 437, 225, 103)
        self.history_lab.clicked.connect(lambda: print("historylab clicked")) # TODO: Put history window here
        
        self.settings_lab = ClickableLabel(self.main)
        self.settings_lab.setObjectName("settingslab")
        self.settings_lab.setStyleSheet("#settingslab{background-color: transparent;}")
        self.settings_lab.setGeometry(46, 570, 225, 103)
        self.settings_lab.clicked.connect(lambda: print("settingslab clicked")) # TODO: Put settings window here
        
        self.exit_lab = ClickableLabel(self.main)
        self.exit_lab.setObjectName("exitlab")
        self.exit_lab.setStyleSheet("#exitlab{background-color: transparent;}")
        self.exit_lab.setGeometry(46, 703, 225, 103)
        self.exit_lab.clicked.connect(self.main.close)
    def show(self):
        self.main.show()