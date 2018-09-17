import sqlite3

conn = sqlite3.connect('test_db.dbf')
cursor = conn.cursor()
name = "Иванов"
sum = 95
sql_str = "SELECT * FROM EPGU WHERE fio Like '%"+ name +"%'"
print(sql_str)
cursor.execute(sql_str)
A = cursor.fetchall()
print(A)
for i in A:
    print(i[1])
    if i[1]==sum:
        print('found=',i)



conn.commit()
conn.close()