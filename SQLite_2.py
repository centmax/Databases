#Five steps for interacting with Databases
# 1 Connect to a Database
# 2 Create a cursor object
# 3 Write an SQL querry
# 4. Commit changes
# 5. Close a Database Connection

import sqlite3

def create_table():
    conn= sqlite3.connect("lite.db")
    cur= conn.cursor()
    cur.execute ("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert (item, quantity, price):
    conn= sqlite3.connect("lite.db")
    cur= conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price ))
    conn.commit()
    conn.close()

insert('coffee cup', 10, 200 )

def view():        # viewing the database inputs
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close
    return rows
print (view())

