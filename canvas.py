import sys

from PyQt5 import QtCore, QtGui, uic, QtWidgets 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton,QAction, QShortcut
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt,pyqtSlot


class Canvas(QtWidgets.QMainWindow):
    def __init__(self, index):
        super().__init__()

        self.label = QtWidgets.QLabel()
        self.whiteboard = QtGui.QPixmap(280,280)
        #self.setStyleSheet("background-color: black;")
        self.label.setPixmap(self.whiteboard)
        self.setCentralWidget(self.label)
        self.index = index
        #self.count = 0
        self.last_x, self.last_y = None, None
    
    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()
            return

        cursor = QtGui.QPainter(self.label.pixmap())
        p = QtGui.QPen()
        p.setWidth(12)
        p.setColor(QtGui.QColor('#FFFFFF'))
        cursor.setPen(p)
        cursor.drawLine(self.last_x, self.last_y, e.x(), e.y())
        cursor.end()
        self.update()
    
        # update the origin for the next event
        self.last_x = e.x()
        self.last_y = e.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def save(self):
        p = QWidget.grab(self)
        p_resized = p.scaled(28,28,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        fileName = "image/"+ str(self.index) +".jpeg"
        p_resized.save(fileName, 'JPEG')
        print("image saved!")
        

        self.close()

def save_all(lst_wind):
    for i in lst_wind:
        i.save()

def canvases():
    app = QtWidgets.QApplication(sys.argv)
 
    windows = []
    shortcuts = []
    for i in range(5):
        windows.append(Canvas(i))
        windows[i].setWindowFlags(QtCore.Qt.FramelessWindowHint)
        windows[i].move(340+i*300,400)
        shortcuts.append(QShortcut(QKeySequence('Ctrl+S'), windows[i]))
        shortcuts[i].activated.connect(lambda: save_all(windows))

    for i in range(5):
        windows[i].show()
    app.exec_()


if __name__ == "__main__":
    canvases()
    
