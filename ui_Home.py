import sys
import os
import ui_Register
import ast
import customWid_Profile
import customWidget_homeMenu
import sqlite3
import pyqtgraph as pg
from pathlib import Path, PureWindowsPath
from customWidget_insertData import customWidget_insertData
from images import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class ui_Home(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #Width:1200, Height:700
        self.setFixedSize(1200,600)
        self.resize(1200,600)
        layout = QGridLayout()

        connectdb = sqlite3.connect(os.path.join(sys.path[0], 'Database\WeatherDb.db'))
        cur = connectdb.cursor()
        result = cur.execute('SELECT * FROM weather_data;')
        data = result.fetchall()

        #rows = cur.execute('SELECT  FROM wather_data')

        #Graph Widget
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = []
        temperature = []

        for rows in data:
            hour.append(int(rows[1]))
            temperature.append(rows[2])

        # plot data: x, y values
        self.graphWidget.plot(hour, temperature)
        self.graphWidget.setBackground('w')
        self.graphWidget.setTitle("<span style=\"color:black;font-size:35px\">Temperature</span>")
        self.graphWidget.setLabel('left', "<span style=\"color:red;font-size:30px\">Temperature (°C)</span>")
        self.graphWidget.setLabel('bottom', "<span style=\"color:red;font-size:30px\">TimeStamp (YYYY/MM/DD/HH/MM)</span>")
        self.graphWidget.setFixedSize(900,500)

        self.mainmenu = customWid_Profile.customWid_Profile()

        layout.addWidget(self.mainmenu, 0,0)

        #QtStacked Layout
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.graphWidget)

        #layout.addWidget(customWidget_homeMenu.customWidget_homeMenu(),1,0)
        layout.setAlignment(Qt.AlignCenter)
        layout.setAlignment(Qt.AlignTop)

        #Table Data Layout
        self.tableWidget = QTableWidget()
        #self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Index'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Timestamp'))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem('Temperature'))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem('Humidity'))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem('Percipitation'))
        self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem('Cloud Cover'))
        self.tableWidget.setHorizontalHeaderItem(6, QTableWidgetItem('Wind Speed'))
        self.tableWidget.setHorizontalHeaderItem(7, QTableWidgetItem('Wind Direction'))
        self.stackedWidget.addWidget(self.tableWidget)

        #Insert Data
        self.insertDataWidget = customWidget_insertData()
        self.stackedWidget.addWidget(self.insertDataWidget)

        #Button States
        self.mainmenu.home_button.clicked.connect(lambda: self.on_home_button_clicked())
        self.mainmenu.prediction_button.clicked.connect(lambda: self.on_prediction_button_clicked())
        self.mainmenu.upload_button.clicked.connect(lambda: self.on_upload_button_clicked())
        self.mainmenu.singout_button.clicked.connect(lambda: self.on_signout_clicked())

        self.stackedWidget.setCurrentIndex(0)
        layout.addWidget(self.stackedWidget, 0, 1)
        widget = QWidget()
        widget.setLayout(layout)

        #layout.addLayout(self.finalLayout)
        #self.setStyleSheet("background-color: rgb(153, 204, 255)")
        self.setCentralWidget(widget)

    def LoadData(self):
        self.conn = sqlite3.connect(os.path.join(sys.path[0], 'Database\WeatherDb.db'))

        cur = self.conn.cursor()
        rows = cur.execute('SELECT * FROM weather_data')
        data = cur.fetchall()
        
        for row in data:
            self.addTable(self.MyConverter(row))

        cur.close()

    def addTable(self, columns):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        for i, column in enumerate(columns):
            self.tableWidget.setItem(rowPosition, i, QTableWidgetItem(str(column)))

    def MyConverter(self, mydata):
        def cvt(data):
            try: 
                return ast.literal_eval(data)
            except Exception:
                return str(data)
        return tuple(map(cvt, mydata))


    def on_home_button_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        connectdb = sqlite3.connect(os.path.join(sys.path[0], 'Database\WeatherDb.db'))
        cur = connectdb.cursor()
        result = cur.execute('SELECT * FROM weather_data;')
        data = result.fetchall()
        self.setFixedSize(1200,600)
        hour = []
        temperature = []

        for rows in data:
            hour.append(int(rows[1]))
            temperature.append(rows[2])

        # plot data: x, y values
        self.graphWidget.plot(hour, temperature)
        #self.graphWidget.show()
        return

    def on_prediction_button_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.LoadData()
        self.setFixedSize(1200,600)
        #self.graphWidget.hide()

        return
    
    def on_upload_button_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
        self.setFixedSize(700,600)
        return
    
    def signout_button_clicked(self):
        return

    def on_signout_clicked(self):
        sys.exit(0)
        return

    def show(self, userinfo = 'Username'):
        QMainWindow.show(self)
        self.userinfo = userinfo
        print(self.userinfo)
        self.mainmenu.profilelabel.setText(self.userinfo[2])


        #FOR MENU BAR Width:300, HeightL:700


if __name__ == '__main__':
    app = QApplication([])
    window = ui_Home()
    cond = window.show()
    sys.exit(app.exec_())  