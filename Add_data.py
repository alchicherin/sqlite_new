import sqlite3
import random


conn = sqlite3.connect('test_db.dbf')

for i in range(1000000):
    card = str(random.randint(100000,999999))+"******"+str(random.randint(1000,9999))
    print(card)
    sum = str(random.randint(1,1000))
    print(sum)
    fio = "LastNAme First Name" + str(i) + str(random.randint(1,100))
    print(fio)
    INN = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    print(INN)
    ID = "ep" + str(random.getrandbits(32)) + str(random.getrandbits(16))
    print(ID)

    sql_str = "INSERT INTO EPGU VALUES('"+card+"',"+sum+", '"+fio+"','"+INN+"','"+ID+"')"
#sql_str = "INSERT INTO EPGU VALUES('4874++++++8876',500, 'Иванов Иван Иванович','')"
    conn.execute(sql_str)
conn.commit()
conn.close()