import sys
import os
import ui_Login
import PyQt5
import sqlite3
from pathlib import Path, PureWindowsPath
from images import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class customWidget_insertData(QWidget):
    def __init__(self,*args, **kwargs):
        super(customWidget_insertData, self).__init__(*args, **kwargs)
        self.layout = QGridLayout()
        self.layout1 = QVBoxLayout()

        #Labels
        title_label = QLabel()
        title_label.setFixedHeight(50)
        date_label = QLabel('Timestamp(YYYYMMDDHHMM): ')
        temp_label = QLabel('Temperature: ')
        hum_label = QLabel('Humidity: ')
        prec_label = QLabel('Percipitation: ')
        cloud_label = QLabel('Cloud Cover: ')
        wind_speed_label = QLabel('Wind Speed: ')
        wind_direction_label = QLabel('Wind Direction: ')

        self.date_textbox = QLineEdit()
        self.temp_textbox = QLineEdit()
        self.hum_textbox = QLineEdit()
        self.prec_textbox = QLineEdit()
        self.cloud_textbox = QLineEdit()
        self.wind_speed_textbox = QLineEdit()
        self.wind_direction_textbox = QLineEdit()

        self.submit_button = QPushButton('Submit')
        self.clear_button = QPushButton('Clear')

        self.layout.addWidget(title_label,0,0)
        self.layout.addWidget(date_label,1,0)
        self.layout.addWidget(temp_label,2,0)
        self.layout.addWidget(hum_label,3,0)
        self.layout.addWidget(prec_label,4,0)
        self.layout.addWidget(cloud_label,5,0)
        self.layout.addWidget(wind_speed_label,6,0)
        self.layout.addWidget(wind_direction_label,7,0)
        self.layout.addWidget(self.date_textbox,1,1)
        self.layout.addWidget(self.temp_textbox,2,1)
        self.layout.addWidget(self.hum_textbox,3,1)
        self.layout.addWidget(self.prec_textbox,4,1)
        self.layout.addWidget(self.cloud_textbox,5,1)
        self.layout.addWidget(self.wind_speed_textbox,6,1)
        self.layout.addWidget(self.wind_direction_textbox,7,1)

        self.layout1.addLayout(self.layout)
        #self.layout1.addSpacing()
        self.layout1.addStretch()
        self.layout1.setAlignment(Qt.AlignTop)
        self.layout1.addWidget(self.submit_button)
        self.layout1.addWidget(self.clear_button)

        self.submit_button.clicked.connect(lambda: self.on_submit_clicked())
        self.clear_button.clicked.connect(lambda: self.on_clear_clicked())


        self.setLayout(self.layout1)
        self.setFixedSize(400,500)
        return

    def on_submit_clicked(self):
        self.conn = sqlite3.connect(os.path.join(sys.path[0], 'Database\WeatherDb.db'))

        cur = self.conn.cursor()
        rows = cur.execute('SELECT * FROM weather_data WHERE "index" = (SELECT MAX("index") FROM weather_data);')
        data = cur.fetchall()
        data = data[0]
        print(data[0]+1)
        x = []
        x.append(int(data[0]+1))
        x.append(str(self.date_textbox.text()))
        x.append(str(self.temp_textbox.text()))
        x.append(int(self.hum_textbox.text()))
        x.append(int(self.prec_textbox.text()))
        x.append(int(self.cloud_textbox.text()))
        x.append(int(self.wind_speed_textbox.text()))
        x.append(int(self.wind_direction_textbox.text()))

        sql = 'INSERT INTO weather_data("index", timestamp, temperature, humidity, precipitation, cloud_cover, wind_speed, wind_direction) VALUES(?, ?, ?, ?, ?, ?, ?, ?);'
        cur.execute(sql,x)
        self.conn.commit()
        return

    def on_clear_clicked(self):
        self.date_textbox.setText('')
        self.temp_textbox.setText('')
        self.hum_textbox.setText('')
        self.prec_textbox.setText('')
        self.cloud_textbox.setText('')
        self.wind_speed_textbox.setText('')
        self.wind_direction_textbox.setText('')

if __name__ == '__main__':
    app = QApplication([])
    volume = customWidget_insertData()
    volume.show()
    app.exec_()
