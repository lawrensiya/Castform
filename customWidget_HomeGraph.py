import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5.QtWidgets import *
import numpy as np

class customWidget_HomeGraph(QWidget):
    def __init__(self):
        win = pg.plot()
        win.setWindowTitle('pyqtgraph BarGraphItem')

        # create list of floats
        y1 = np.linspace(0, 20, num=20)

        # create horizontal list
        x = np.arange(20)

        # create bar chart
        bg1 = pg.BarGraphItem(x=x, height=y1, width=0.6, brush='r')
        win.addItem(bg1)

## Start Qt event loop unless running in interactive mode or using 
if __name__ == '__main__':
    app = QApplication([])
    window = ui_Home()
    cond = window.show()
    sys.exit(app.exec_())  