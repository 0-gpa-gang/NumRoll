import sqlite3
import os

# import the following lines to the main py file
# conn = sqlite3.connect("image.db")
# c = conn.cursor()


def read_from_db():
    conn = sqlite3.connect("image.db")
    c = conn.cursor()
    c.execute("SELECT * FROM image")
    total = []
    for row in c.fetchall():
        total.append(row[0])
    return total


def output_to_db(classify):
    conn = sqlite3.connect("image.db")
    c = conn.cursor()
    for i in classify:
        c.execute("INSERT INTO image (classifier) VALUES (?)", i)
        conn.commit()
    hi = []
    for row in c.fetchall():
        hi.append(row[1])
    print(hi)

def special_case():
    conn = sqlite3.connect("image.db")
    c = conn.cursor()
    c.execute("SELECT * FROM image")
    special = ""
    for row in c.fetchall():
        special += row[1]
    if special == "42069":
        os.system("vlc RickRoll.mp4")


print(read_from_db())