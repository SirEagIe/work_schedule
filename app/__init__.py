import tkinter as tk
import sqlite3 as sql
from app.MainApplication import MainApplication
from importlib import resources

connection = sql.connect('test.db')
with connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `test` (name TEXT, date TEXT, time1 TEXT, time2 TEXT)")
    cursor.execute("SELECT * FROM `test`")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()