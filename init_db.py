import sqlite3

conn = sqlite3.connect('dados_mainframe.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS data
                (created TEXT PRIMARY KEY NOT NULL,
                ram TEXT NOT NULL,
                cpu TEXT NOT NULL,
                disk TEXT NOT NULL);''')

conn.commit()
conn.close()




