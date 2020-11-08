import sys
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic

def window():
    # create instance of QApplication
    # sys.argv contains command link arguments 
    app = QApplication(sys.argv)

    #create the GUI
    widget = QWidget()
    widget.setWindowTitle("NumRoll")
    
    # (x,y,width, height)
    widget.setGeometry(150,150,1500,1500)
    widget.move(1170, 330)
    welcomemsg = QLabel('<h1>Your Homework is Locked!</h1>', parent=widget)
    welcomemsg.move(100,200)
    instruction = QLabel('<h3>Toggle your mouse to write down your 5-bit passcode</h3>', parent = widget)
    instruction.move(60, 40)


    # make the buttons
    start = QPushButton(widget)
    start.setText("Click here to start.")
    start.move(65,150)
    start.clicked.connect(start_pushed)

    # show the window
    widget.show()

    # execute the program
    sys.exit(app.exec_())

def start_pushed():
    os.system("python3 canvas.py")


if __name__ == "__main__":
    window()