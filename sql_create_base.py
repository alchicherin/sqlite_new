import sqlite3

conn = sqlite3.connect('test_db.dbf')
sql_str = "CREATE TABLE EPGU (card text,sum float, fio text, INN text,ID text primary key)"
conn.execute(sql_str)
conn.commit()
conn.close()