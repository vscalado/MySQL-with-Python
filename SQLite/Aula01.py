import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Naruto(id REAL, nome TEXT, clã TEXT)")


def data_entry():
    c.execute("INSERT INTO Naruto VALUES(1,'Sasuke','Uchiha')")

    conn.commit()
    c.close()
    conn.close()


#create_table()
data_entry()
