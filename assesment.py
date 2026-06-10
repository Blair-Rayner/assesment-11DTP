#docstring - Blair Rayner - cyclists database application
#imports
import sqlite3 

#constants and variables
DATABASE = 'assesment.db'


#functions
def print_all_cyclists():
    '''print all cyclists'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM cyclists;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results
    print(f"{'Name:':<22} {'Team:':<26} {'Top speed:':<12} {'Average speed:':<18} {'Nationality:':<15}")
    for cyclist in results:
        print(f"{cyclist[1]:<22} {cyclist[2]:<26} {cyclist[3]:<12} {cyclist[4]:<18} {cyclist[5]:<15}")
    #loop finished
    db.close()

def print_cyclists_by_top_speed():
    '''print cyclists ordered by top speed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM cyclists ORDER BY top_speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results
    print(f"{'Name:':<22} {'Team:':<26} {'Top speed:':<12} {'Average speed:':<18} {'Nationality:':<15}")
    for cyclist in results:
        print(f"{cyclist[1]:<22} {cyclist[2]:<26} {cyclist[3]:<12} {cyclist[4]:<18} {cyclist[5]:<15}")
    #loop finished
    db.close()

def print_cyclists_by_average_speed():
    '''print cyclists ordered by average speed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM cyclists ORDER BY avg_speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results
    print(f"{'Name:':<22} {'Team:':<26} {'Top speed:':<12} {'Average speed:':<18} {'Nationality:':<15}")
    for cyclist in results:
        print(f"{cyclist[1]:<22} {cyclist[2]:<26} {cyclist[3]:<12} {cyclist[4]:<18} {cyclist[5]:<15}")
    #loop finished
    db.close()

def print_cyclists_by_nationality():
    '''print cyclists ordered by nationality'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM cyclists ORDER BY nationality ASC, top_speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results
    print(f"{'Name:':<22} {'Team:':<26} {'Top speed:':<12} {'Average speed:':<18} {'Nationality:':<15}")
    for cyclist in results:
        print(f"{cyclist[1]:<22} {cyclist[2]:<26} {cyclist[3]:<12} {cyclist[4]:<18} {cyclist[5]:<15}")
    #loop finished
    db.close()

def print_cyclists_alphabetically():
    '''print cyclists ordered alphabetically'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM cyclists ORDER BY rider_name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results
    print(f"{'Name:':<22} {'Team:':<26} {'Top speed:':<12} {'Average speed:':<18} {'Nationality:':<15}")
    for cyclist in results:
        print(f"{cyclist[1]:<22} {cyclist[2]:<26} {cyclist[3]:<12} {cyclist[4]:<18} {cyclist[5]:<15}")
    #loop finished
    db.close()

def print_cyclists_by_team():
    '''print cyclists ordered by team'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM cyclists ORDER BY team ASC, top_speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through results
    print(f"{'Name:':<22} {'Team:':<26} {'Top speed:':<12} {'Average speed:':<18} {'Nationality:':<15}")
    for cyclist in results:
        print(f"{cyclist[1]:<22} {cyclist[2]:<26} {cyclist[3]:<12} {cyclist[4]:<18} {cyclist[5]:<15}")
    #loop finished
    db.close()

#main code
while True:
    user_input = input("Choose a format: \n1. Print all cyclists \n2. Order cyclists by top speed \n3. Order cyclists by average speed \n4. Order cyclists by nationality \n5. Order cyclists alphabetically  \n6. Order cyclists by team \n7. Exit \n")
    if user_input == '1':
        print_all_cyclists()
    elif user_input == '2':
        print_cyclists_by_top_speed()
    elif user_input == '3':
        print_cyclists_by_average_speed()
    elif user_input == '4':
        print_cyclists_by_nationality()
    elif user_input == '5':
        print_cyclists_alphabetically()
    elif user_input == '6':
        print_cyclists_by_team()
    elif user_input == '7':
        print("Exiting program...")
        break
    else:
        print("Invalid input, please try again. ")