import sys
import os
import ui_Register
import ui_Home
import sqlite3
from pathlib import Path, PureWindowsPath
from images import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class ui_Login(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.conn = sqlite3.connect(os.path.join(sys.path[0], 'Database\WeatherDb.db'))
        self.setWindowTitle('Client Login')
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setLayout(self.loginLayout())

        #Add BG
        self.setAutoFillBackground(True)

        self.resize(300,200)

    def AppShow(self):
        QDialog.show(self)
        self.bool = True
        return self.bool

    def loginLayout(self):
            self.layout = QVBoxLayout()
            inv = QLabel()
            inv1 = QLabel()
            inv2 = QLabel()

            #Image
            imageLabel = QLabel()
            pixmap = QPixmap(os.path.join(sys.path[0], 'images\weather-icon.png'))
            imageLabel.setPixmap(pixmap)
            imageLabel.setAlignment(Qt.AlignCenter)

            #Username
            textLabel1 = QLabel('UserName: ')
            self.usernamebox = QLineEdit()
            usrLayout = QHBoxLayout()
            usrLayout.addWidget(textLabel1)
            usrLayout.addWidget(self.usernamebox)

            #Passowrd
            textLabel2 = QLabel('Password: ')
            self.passwordbox = QLineEdit()
            self.passwordbox.setEchoMode(QLineEdit.Password)
            passLayout = QHBoxLayout()
            passLayout.addWidget(textLabel2)
            passLayout.addWidget(self.passwordbox)

            #Gird Layout
            boxLayout = QGridLayout()
            boxLayout.addWidget(textLabel1,0,0)
            boxLayout.addWidget(self.usernamebox,0,1)
            boxLayout.addWidget(textLabel2,1,0)
            boxLayout.addWidget(self.passwordbox,1,1)

            #Button
            loginButton = QPushButton('Login')
            exitButton = QPushButton('Exit')
            adminButton = QPushButton('Login as Admin')
            registerButton = QPushButton('Register')
            buttonLayout = QHBoxLayout()
            buttonLayout.addWidget(loginButton)
            buttonLayout.addWidget(exitButton)

            exitButton.clicked.connect(self.on_exitClicked)
            loginButton.clicked.connect(self.on_loginClicked)
            registerButton.clicked.connect(self.on_registerClicked)
            
            self.layout.addWidget(imageLabel)
            self.layout.addWidget(inv)
            self.layout.addWidget(inv1)
            self.layout.addLayout(boxLayout)
            self.layout.addWidget(inv2)
            self.layout.addLayout(buttonLayout)
            self.layout.addWidget(adminButton)
            self.layout.addWidget(registerButton)

            return self.layout

    @pyqtSlot()
    def on_exitClicked(self):
        sys.exit(0)

    @pyqtSlot()
    def on_loginClicked(self):
        userdata = []
        cursor = self.conn.execute('SELECT user_id, username, first_name, last_name, password, privilage from users')
        for row in cursor:
            if row[1] == self.usernamebox.text() and row[4] == self.passwordbox.text():
                self.window = ui_Home.ui_Home()
                self.hide()
                self.window.show(row)
                return
        msg = QMessageBox()
        msg.setWindowTitle('Warning!')
        pixmap = QPixmap(32,32)
        pixmap.fill(Qt.transparent)
        msg.setWindowIcon(QIcon(pixmap))
        msg.setText('Username or password Incorrect.')
        msg.exec_()

    @pyqtSlot()
    def on_registerClicked(self):
        self.window = ui_Register.ui_Register()
        self.hide()
        self.window.exec_()
    

if __name__ == '__main__':
    app = QApplication([])
    window = ui_Login()
    cond = window.AppShow()  
    sys.exit(app.exec_())          