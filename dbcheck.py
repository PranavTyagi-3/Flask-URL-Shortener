import sqlite3

conn=sqlite3.connect('urlbase.db')

cur=conn.execute("select * from urls")
for i in cur:
    print(i)