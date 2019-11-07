import sqlite3
from sqlite3 import Error
conn=sqlite3.connect('test.db')
print("opened database sucessfully")
conn.execute('''Create Table STUDENTS(ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50));''')
print("Table created")
conn.execute("INSERT INTO STUDENTS(ID,NAME,AGE,ADDRESS) VALUES(1,'SAURAV',20,'TANDI')")
conn.execute("INSERT INTO STUDENTS(ID,NAME,AGE,ADDRESS) VALUES(2,'DEV',21,'DHANESHWOR')")
conn.execute("INSERT INTO STUDENTS(ID,NAME,AGE,ADDRESS) VALUES(3,'DIVS',20,'MAHARAJGUNJ')")
conn.execute("INSERT INTO STUDENTS(ID,NAME,AGE,ADDRESS) VALUES(4,'GAURAV',19,'KANAKAPURA ROAD')")

print("inserted sucessully")
cur=conn.execute("SELECT ID, NAME, AGE, ADDRESS FROM STUDENTS")
for row in cur:
    print("-"*10)
    print("ID: ", row[0])
    print("NAME: ", row[1])
    print("AGE: ", row[2])
    print("ADDRESS: ", row[3]),"\n"
    print("-"*10)
    
print("operations done sucessfully")

conn.execute("UPDATE STUDENTS set ADDRESS= 'HATTISAR' where ID=1")
conn.commit

cur=conn.execute("SELECT ID, NAME, AGE, ADDRESS FROM STUDENTS")
for row in cur:
    print("-"*10)
    print("ID: ", row[0])
    print("NAME: ", row[1])
    print("AGE: ", row[2])
    print("ADDRESS: ", row[3]),"\n"
    print("-"*10)
   
print("operations done sucessfully")

conn.execute("DELETE FROM STUDENTS where ID=2")
conn.commit

cur=conn.execute("SELECT ID, NAME, AGE, ADDRESS FROM STUDENTS")
for row in cur:
    print("-"*10)
    print("ID: ", row[0])
    print("NAME: ", row[1])
    print("AGE: ", row[2])
    print("ADDRESS: ", row[3]),"\n"
    print("-"*10)
  
print("operations done sucessfully")
conn.commit
conn.close()



                 


    
    

