import sqlite3
# persistent table/column error solved by renaming the table from book to book_1

# connect front end and back-end interfaces

def connect():
    conn = sqlite3.connect("../DATABASES/books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book_1 (id INTEGER PRIMARY KEY, title text, author text,year integer, isbn integer)")
    conn.commit()
    conn.close()


### First code is for data entry ie author, title, year, ISBN
def insert(title, author, year, isbn):
    conn = sqlite3.connect("../DATABASES/books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book_1 VALUES (NULL,?,?,?,?)",(title, author, year, isbn) )
    conn.commit()
    conn.close()

    # Create view function


def view():
    conn = sqlite3.connect("../DATABASES/books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book_1")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# work on Search function
def search (title= "", author="", year="", isbn=""):   # equal== after allows user to also querry by name/ inputs
    conn = sqlite3.connect("../DATABASES/books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book_1 WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete (id):
    conn = sqlite3.connect("../DATABASES/books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book_1 WHERE id=?", (id,) )
    conn.commit()
    conn.close()

def update ( title, author, year, isbn, id):
    conn = sqlite3.connect("../DATABASES/books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book_1 SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()

# insert('good the bad and ugly', 'Jack', 1922, 1177)
# insert('good cop bad', 'maurice', 1912, 11966)
# # delete(3)
# print(view())
update(4, "cops gone rougue", "Mari", 2012, 114223)
print(search(author="Jack"))
