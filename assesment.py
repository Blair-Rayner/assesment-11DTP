import sqlite3 

db = sqlite3.connect('/Users/blairrayner/Downloads/assesment.db')
cursor = db.cursor()
sql = "SELECT * FROM assesment;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()
