#docstring - Blair Rayner - assesment database application
#imports
import sqlite3 

#constants and variables
DATABASE = '/Users/blairrayner/Downloads/assesment.db'


#functions
def print_all_cyclists():
    '''print all cyclists'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM assesment;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results
    for cyclist in results:
        print(f"{cyclist[1]:<22} {cyclist[2]:<25} {cyclist[3]:<3} {cyclist[4]:<5} {cyclist[5]:<15}")
    #loop finished
    db.close()



#main code
print_all_cyclists()
