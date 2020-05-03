import sys
import os
import ui_Login
import PyQt5
from pathlib import Path, PureWindowsPath
from images import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class customWidget_homeMenu(QWidget):
    def __init__(self,*args, **kwargs):
        super(customWidget_homeMenu, self).__init__(*args, **kwargs)
        self.layout = QVBoxLayout()

        #Home Button
        self.home_button = QPushButton('Home')
        self.home_button.setFixedHeight(50)

        #Prediction Button
        self.prediction_button = QPushButton('Data Table')
        self.prediction_button.setFixedHeight(50)

        #Upload Data
        self.upload_button = QPushButton('Upload Data')
        self.upload_button.setFixedHeight(50)

        #Signout Button
        self.singout_button = QPushButton('Sign Out')
        self.singout_button.setFixedHeight(50)

        self.layout.addWidget(self.home_button)
        self.layout.addWidget(self.prediction_button)
        self.layout.addWidget(self.upload_button)
        self.layout.addWidget(self.singout_button)
        self.setLayout(self.layout)

        
        self.setFixedSize(250, 350)
        return

if __name__ == '__main__':
    app = QApplication([])
    volume = customWidget_homeMenu()
    volume.show()
    app.exec_()