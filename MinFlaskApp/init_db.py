import sqlite3

connection = sqlite3.connect('database.sqlite')


with open('setup.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()