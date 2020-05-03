import sys
import os
import ui_Login
import PyQt5
from pathlib import Path, PureWindowsPath
from images import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class  customWid_Profile(QWidget):
    def __init__(self, *args, **kwargs):
        super(customWid_Profile, self).__init__(*args, **kwargs)
        self.layout = QVBoxLayout()

        #Image
        image = QPixmap('images/profile.png')
        self.labelimage = QLabel()
        self.labelimage.setPixmap(image.scaled(150, 150, Qt.KeepAspectRatio))
        self.labelimage.setAlignment(Qt.AlignCenter)

        #label
        self.profilelabel = QLabel('Username')
        self.profilelabel.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.profilelabel.setFont(font)

        #Home Button
        self.home_button = QPushButton('Home')
        self.home_button.setFixedHeight(50)

        #Prediction Button
        self.prediction_button = QPushButton('Table Data')
        self.prediction_button.setFixedHeight(50)

        #Upload Data
        self.upload_button = QPushButton('Upload Data')
        self.upload_button.setFixedHeight(50)

        #Signout Button
        self.singout_button = QPushButton('Sign Out')
        self.singout_button.setFixedHeight(50)


        #Layout
        self.layout.addStretch()
        self.layout.addWidget(self.labelimage)
        self.layout.addWidget(self.profilelabel)
        self.layout.addSpacing(20)
        self.layout.addWidget(self.home_button)
        self.layout.addWidget(self.prediction_button)
        self.layout.addWidget(self.upload_button)
        self.layout.addSpacing(40)
        self.layout.addWidget(self.singout_button)

        widget_arrangement = QWidget()
        widget_arrangement.setLayout(self.layout)

        self.finalLayout = QStackedLayout()
        BG = QWidget()
        BG.setStyleSheet('background-color: gray')

        self.finalLayout.setStackingMode(QStackedLayout.StackAll)
        self.finalLayout.addWidget(BG)
        self.finalLayout.addWidget(widget_arrangement)

        

        self.setLayout(self.finalLayout)
        self.setFixedSize(200,520)
        return

    def setUsername(self, user):
        self.profilelabel.setText(user)


if __name__ == '__main__':
    app = QApplication([])
    volume = customWid_Profile()
    volume.show()
    app.exec_()