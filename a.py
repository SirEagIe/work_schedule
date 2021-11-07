import sqlite3 as sql

connection = sql.connect('test.db')
with connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `test`")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()