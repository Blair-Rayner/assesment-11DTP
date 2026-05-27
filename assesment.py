#docstring - Blair Rayner - assesment database application
#imports
import sqlite3 

#constants and variables
DATABASE = '/Users/blairrayner/Downloads/assesment.db'


#functions
def print_all_cyclists():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM assesment;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close()



#main code

