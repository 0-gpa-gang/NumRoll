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
            ('image/0.jpeg'),
            ('image/1.jpeg'),
            ('image/2.jpeg'),
            ('image/3.jpeg'),
            ('image/4.jpeg');""")
    conn.commit()

if __name__ == "__main__":
    create()
