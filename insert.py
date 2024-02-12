import sqlite3
conn = sqlite3.connect('afternoon.db')
print("Opened database successfully")

conn.execute(("INSERT INTO EMPLOYEES VALUES (1,'FAITH KARIMI',35,340000.00)"))
conn.execute(("INSERT INTO EMPLOYEES VALUES (2,'JOHN MBUGUA',45,375000.00)"))
conn.execute(("INSERT INTO EMPLOYEES VALUES (3,'GLORY MUTUKU',25,160000.00)"))
conn.execute(("INSERT INTO EMPLOYEES VALUES (4,'MARK NJENGA',37,240000.00)"))
conn.execute(("INSERT INTO EMPLOYEES VALUES (5,'KYELI JENA',38,290000.00)"))

conn.commit()
print("Emoployee inserted successfully")
conn.close()