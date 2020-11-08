import sys
import os

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic
import numpy as np
from classifier import *
from canvas import *
import sqlite3


def window():
    # create instance of QApplication
    # sys.argv contains command link arguments 
    app = QApplication(sys.argv)

    #create the GUI
    widget = QWidget()
    widget.setWindowTitle("NumRoll")
    
    # (x,y,width, height)
    widget.setGeometry(150,150,1500,700)
    widget.move(1170, 330)
    welcomemsg = QLabel('<h1>Your Homework is Locked!</h1>', parent=widget)
    welcomemsg.move(350,60)
    instruction = QLabel('<h3>Toggle your mouse to write down your 5-bit passcode</h3>', parent = widget)
    instruction.move(250,120)
    instruction2 = QLabel('<h3>When you are done, Press "Ctrl+S" to proceed.</h3>', parent = widget)
    instruction2.move(340,600)

    # make the buttons
    start = QPushButton(widget)
    start.setStyleSheet("background-color:red")
    start.setText("Click here to start.")
    start.move(600,180)
    start.clicked.connect(start_pushed)

    # show the window
    widget.show()

    # execute the program
    sys.exit(app.exec_())

def start_pushed():
    os.system("python3 canvas.py")
    classify_and_save()
    compare('12345')

def compare(passcode):
    conn = sqlite3.connect("image.db")
    c = conn.cursor()
    c.execute("""SELECT classifier FROM image""")

    #print(str(c.fetchall()))
    code = []
    for i in c.fetchall():
        code.append(str(i[0]))
    a = "".join(code)
    print(a)

    if a == passcode:
        os.system("vim homework.txt")
    elif a == "42069":
        os.system("vlc RickRoll.mp4")
    else:
        print("Wrong code")
        os.system("python3 error.py")


if __name__ == "__main__":
    window()

