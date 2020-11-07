import sys

from PyQt5 import QtCore, QtGui, uic, QtWidgets 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,pyqtSlot


class Canvas(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        whiteboard = QtGui.QPixmap(900,900)
        self.label.setPixmap(whiteboard)
        self.setCentralWidget(self.label)
#        self.mousePressed()
#        self.mouseReleased()
#        self.draw()
     
        self.last_x, self.last_y = None, None

#    def draw(self):
#        painter = QtGui.QPainter(self.label.pixmap())
#        pen = QtGui.QPen()
#        pen.setWidth(40)
#        pen.setColor(QtGui.QColor('red'))
#        painter.setPen(pen)
#        painter.drawPoint(450,450)
#        painter.end() 
    
    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()
            return

        cursor = QtGui.QPainter(self.label.pixmap())
        p = QtGui.QPen()
        p.setWidth(30)
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

    def saveImage():
        pass
        
def window():
    app = QtWidgets.QApplication(sys.argv)
    window = Canvas()

    button = QtWidgets.QPushButton(window)
    button.setText("finish")
    button.move(60,15)
    button.clicked.connect(button_pushed)

    window.show()

    sys.exit(app.exec_())

def button_pushed():
    print("ready to quit")

    
if __name__ == "__main__":
    window()
