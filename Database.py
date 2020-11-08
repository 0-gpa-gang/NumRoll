import sqlite3
def create():
    conn = sqlite3.connect('image.db')

    c = conn.cursor()
    c.execute("""DROP TABLE image""")

    c.execute("""CREATE TABLE image (
            path TEXT PRIMARY KEY,
            classifier INTEGER DEFAULT "N/A"
            )""")

    c.execute("""INSERT INTO image (path)
            VALUES
            ('image/1.jpg'),
            ('image/2.jpg'),
            ('image/3.jpg'),
            ('image/4.jpg'),
            ('image/5.jpg');""")
    conn.commit()



create()