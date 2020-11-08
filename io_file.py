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
    total = read_from_db()
    for i in range(len(classify)):
        num = classify[i]
        location = total[i]
        c.execute("UPDATE image SET classifier = (?) WHERE path = (?)", (num, location))
        conn.commit()
    # if want to see the classified result in a printed list, turn docstring into code
    """
    classified = []
    c.execute("SELECT * FROM image")
    for row in c.fetchall():
        classified.append(row[1])
    print(classified)
    """

def special_case():
    conn = sqlite3.connect("image.db")
    c = conn.cursor()
    c.execute("SELECT * FROM image")
    special = ""
    for row in c.fetchall():
        special += str(row[1])
    if special == "42069":
        os.system("vlc RickRoll.mp4")  # change with system
