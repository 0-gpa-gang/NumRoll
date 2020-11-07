import sqlite3

conn= sqlite3.connect('image.db')

c = conn.cursor()

c.execute("""DROP TABLE image""")

c.execute("""CREATE TABLE image (
            path TEXT PRIMARY KEY,
            classfier INTEGER DEFAULT "N/A"
            )""")

c.execute("""INSERT INTO image (path)
            VALUES
            ('image/1.jpeg'),
            ('image/2.jpeg'),
            ('image/3.jpeg'),
            ('image/4.jpeg'),
            ('image/5.jpeg');""")

c.execute("SELECT * FROM image")
print(c.fetchall())

conn.close()