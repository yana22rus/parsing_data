import sqlite3

file = "Data_answer.db"

with sqlite3.connect(file) as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_json TEXT
    )""")


def create_data(data):
    with sqlite3.connect(file) as con:
        cur = con.cursor()

        cur.execute("INSERT INTO Data (data_json) VALUES  (?)", (data,))
