
# 1 Connect to a Database
# 2 Create a cursor object
# 3 Write an SQL querry
# 4. Commit changes
# 5. Close a Database Connection
# Replace the code for SQLite3 with code for Psycopg2
# db will be embedded  in the PostgreSQL installation in the pc
#Go to PostgreSQL installation path on PC and create db using PgAdmin
# replaced sqlite with psycopg2
# pass username, password, port to the connect method
# Call the function using Create_table to check for errors
# go to the database and view inputs-under table, stores
# insert inputs in your database and call out 'insert' command... use %s as placeholders
# apply querry in db store .....SELECT *FROM store.....
# print(view()) to view the db items
# execute dlete function and removed item  ...uranges..


import psycopg2

def create_table():
    conn= psycopg2.connect("dbname='database_1' user='postgres' password='Postgresql_2021' host= 'localhost' port= '5432' ")
    cur= conn.cursor()
    cur.execute ("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert (item, quantity, price):
    conn= psycopg2.connect("dbname='database_1' user='postgres' password='Postgresql_2021' host= 'localhost' port= '5432' ")
    cur= conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price ))
    conn.commit()
    conn.close()

# insert('coffee cup', 10, 200 )

def view():        # viewing the database inputs
    conn= psycopg2.connect("dbname='database_1' user='postgres' password='Postgresql_2021' host= 'localhost' port= '5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close
    return rows

def delete (item):      # delete rows/ input
    conn= psycopg2.connect("dbname='database_1' user='postgres' password='Postgresql_2021' host= 'localhost' port= '5432' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


# UPDATE DATABASE
def update (quantity,price, item):      # update inputs on table
    conn= psycopg2.connect("dbname='database_1' user='postgres' password='Postgresql_2021' host= 'localhost' port= '5432' ")
    cur = conn.cursor()
    cur.execute("UPDATE store  SET quantity=%s, price=%s WHERE item=%s", (quantity,price, item))
    conn.commit()
    conn.close()


# Call the function using Create_table
create_table()
# Call the insert
# insert("Oranges", 10, 300)
# insert("tomatoes", 3, 12)
update(100,200, 'tomatoes')
delete("uranges")
print(view())
