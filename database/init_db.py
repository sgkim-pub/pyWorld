import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

SQL = 'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, email TEXT NOT NULL, passwd TEXT NOT NULL)'
cursor.execute(SQL)

cursor.close()
conn.close()
