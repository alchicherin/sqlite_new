import sqlite3

conn = sqlite3.connect('test_db.dbf')
sql_str = "ALTER TABLE EPGU add column ID text "
conn.execute(sql_str)
conn.commit()
conn.close()