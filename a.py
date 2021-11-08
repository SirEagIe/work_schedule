import sqlite3 as sql
import datetime as dt


connection = sql.connect('app.db')
with connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `work_schedule`")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()