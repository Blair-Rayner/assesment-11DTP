import sqlite3 

db = sqlite3.connect('assesment.db')

cursor = db.cursor()


db.close()