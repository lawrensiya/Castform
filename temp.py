import os
import sys
import sqlite3

conn = sqlite3.connect(os.path.join(sys.path[0], 'Database\WeatherDb.db'))
cursor = conn.execute('SELECT username FROM users')

for row in cursor:
    print ('ID = ',row[0])

