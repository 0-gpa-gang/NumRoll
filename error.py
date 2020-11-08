import sys
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic

app = QApplication(sys.argv)

failWindow = QWidget() 
failWindow.setWindowTitle("Error!")
failWindow.setGeometry(150,150,800,300)
failWindow.move(560,560)
failmsg = QLabel('<h2>WRONG CODE! DENIED ACCESS</h2>', parent = failWindow)
failmsg.move(60,60)
failWindow.show()

sys.exit(app.exec_())
