#Five steps for interacting with Databases
# 1 Connect to a Database
# 2 Create a cursor object
# 3 Write an SQL querry
# 4. Commit changes
# 5. Close a Database Connection

import sqlite3
conn= sqlite3.connect("lite.db")
cur= conn.cursor()
cur.execute ("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
cur.execute("INSERT INTO store VALUES ('wine Glass', 8, 10.5 )")
conn.commit()
conn.close()