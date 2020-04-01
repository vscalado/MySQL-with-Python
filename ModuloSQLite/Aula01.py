import sqlite3

conn = sqlite3.connect('bd_estudo.db')
cursor =conn.execute('select * from estados')
rows = cursor.fetchall()
print(rows)
for row in rows:
    print(row)