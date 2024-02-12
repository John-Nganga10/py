import sqlite3

conn = sqlite3.connect('afternoon.db')
print("opened database successfully")

conn.execute('''create table Employees(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
SALARY REAL NOT NULL);''')
print("Table create successfully")
conn.close()