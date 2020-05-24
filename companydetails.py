import sqlite3


def get(self, request, username):        
    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()
    details = "SELECT * FROM softwarecompany WHERE username=?"
    cursor.execute(details, [username])
    
    data=cursor.fetchall()
    print(data)
    return data