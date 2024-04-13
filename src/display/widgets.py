from PyQt5 import QtCore, QtGui, QtWidgets


class ClickableLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        self.clicked.emit()

    clicked = QtCore.pyqtSignal()


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

    def setupUi(self, name, title="default title", parent=None):
        self.main = QtWidgets.QMainWindow(parent)
        self.main.resize(1600, 900)
        self.main.setObjectName(name)
        self.back = ClickableLabel(self.main)
        self.back.setGeometry(0, 0, 30, 30)
        self.main.setWindowTitle(title)

    def close(self):
        super().close()
