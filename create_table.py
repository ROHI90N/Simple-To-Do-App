import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

cursor = conn.cursor()
cursor.execute('''
             CREATE TABLE tasks (task TEXT, task_content TEXT, prio TEXT, dd DATE)''')
print("Created table successfully!")

conn.close()