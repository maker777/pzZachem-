import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout,QStackedLayout,QLineEdit,QTimeEdit,QLCDNumber)
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QColor, QPalette
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("какаято штука")

        Layout = QVBoxLayout()

        widget = QWidget()
        widget.setLayout(Layout)

        delButt = QPushButton("тап")
        delButt.clicked.connect(self.Click)
        Layout.addWidget(delButt)

        self.click = 0
        self.lable = QLabel(f"{self.click}")
        Layout.addWidget(self.lable)

        Layout.addWidget(self.lable)

        self.setCentralWidget(widget)

    def Click(self):
        self.click = self.click + 1
        lable = self.findChild(QLabel).setText(str(self.click))
        


app=QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


