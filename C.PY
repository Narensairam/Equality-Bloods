import sqlite3
conn=sqlite3.connect("students.db")
c = conn.cursor()
c.execute("SELECT UNIT FROM BLOODAVAIL WHERE BLOODGROUP=?",('A+',))
data = c.fetchone()
print(data[0])