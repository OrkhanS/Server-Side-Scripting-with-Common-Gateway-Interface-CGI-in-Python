import sqlite3
import os

def initDatabase():
    print("Initializing the Database")

    if not os.path.isfile('my.db'):
        print("Creating a new Database!!")
        conn = sqlite3.connect("my.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE city
                        (citycode integer PRIMARY KEY, cityname text NOT NULL) 
                    """)

        cursor.execute("""CREATE TABLE softwarecompany
                        (username text type UNIQUE, password text NOT NULL, website text NOT NULL, 
                        nameSoftware text NOT NULL, email text NOT NULL, address text NOT NULL,
                        telephone text NOT NULL, sessionid text DEFAULT -1, located_in integer,
                        FOREIGN KEY (located_in) REFERENCES city (citycode)) 
                    """)

        cursor.execute("""CREATE TABLE internshipposition
                        (id integer PRIMARY KEY, name text NOT NULL, details text NOT NULL, 
                        deadline DATE NOT NULL, expectations text NOT NULL, post text NOT NULL,
                        FOREIGN KEY (post) REFERENCES softwarecompany (username)) 
                    """)

        city = "INSERT INTO city (cityname) VALUES (?)"
        cursor.execute(city, ['Gazimagusa'],)
        cursor.execute(city, ['Girne'],)
        cursor.execute(city, ['Guzelyurt'],)
        cursor.execute(city, ['Iskele'],)
        cursor.execute(city, ['Lefke'],)
        cursor.execute(city, ['Lefkosa'],)
