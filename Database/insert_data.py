import pandas as pd
import os
import sys
from pandas.io import sql
import sqlite3

df = pd.read_csv('Database/data.csv')
#print(df['timestamp'])
list_time = []
for ind, row in enumerate(df['timestamp'].values):
    x = str(row)
    num = 0
    x = x.replace('T', '')
    list_time.append(x)

#df.replace({'timestamp':list}, inplace = True)
df['timestamp'] = list_time

conn = sqlite3.connect('Database/WeatherDb.db')

df.to_sql(con=conn, name='weather_data', if_exists='replace')

conn.commit()
conn.close()






