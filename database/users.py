import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

SQL = 'INSERT INTO users (username, email, passwd) VALUES (?, ?, ?)'
cursor.execute(SQL, ('admin', 'admin@abc.com', 'imsi_00'))
conn.commit()

SQL = 'SELECT * FROM users'
cursor.execute(SQL)
rows = cursor.fetchall()
for row in rows:
    print(row)

SQL = "PRAGMA table_info(users)"
cursor.execute(SQL)
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
