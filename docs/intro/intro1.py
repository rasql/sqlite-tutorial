import sqlite3
connection = sqlite3.connect('demo.db')
cursor = connection.cursor()

connection.close()