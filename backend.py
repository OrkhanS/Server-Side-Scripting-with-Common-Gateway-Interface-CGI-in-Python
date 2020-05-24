import sqlite3
import random
import string  
from datetime import datetime


def register(username, password, name, email, telephone, website, city, postalAddress):
    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()
    newUser = """INSERT INTO softwarecompany 
                        (username, password, website, nameSoftware, email, address, telephone,
                        located_in) VALUES (?, ?, ?, ?, ?, ?, ?, ?) """

    try:
        cursor.execute(newUser, (username, password, website, name, email, postalAddress, telephone, city))
        conn.commit()
    except sqlite3.OperationalError:
        print ("not inserted")


def login(username, password):
    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM softwarecompany WHERE username = ? AND password = ? ", (username, password))
    
    data=cursor.fetchone()[0]

    if data==0:
        return 0

    else:
        flag=1
        while(flag==1):
            randomSessionId = random.randrange(0, 1000000)
            letters = string.ascii_lowercase
            rand_letters = random.choices(letters, k=3)
            result = str(randomSessionId) + rand_letters[0] + rand_letters[1] + rand_letters[2]
            cursor.execute("SELECT count(*) FROM softwarecompany WHERE sessionid = ?", [result])
            flag=cursor.fetchone()[0]

        try:
            cursor.execute("UPDATE softwarecompany SET sessionid = ? WHERE sessionid = -1 AND username=?", (result, username))
            conn.commit()
            print("Logged in successfully")
        except sqlite3.OperationalError:
            print ("not inserted")

        return result


def logOut(sessionid):
    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE softwarecompany SET sessionid = -1 WHERE sessionid = ?", [sessionid])
        conn.commit()
        return True
    except sqlite3.OperationalError:
        print ("Error!")
        return False

def postInternship(sessionid, name, description, expectations, deadline):
    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()
    
    usernameSoftware = "SELECT username FROM softwarecompany WHERE sessionid=?" 
    cursor.execute(usernameSoftware, [sessionid])
    data=cursor.fetchall()

    newPost = "INSERT INTO internshipposition (name, details, deadline, expectations, post) VALUES (?, ?, ?, ?, ?) "

    try:
        cursor.execute(newPost, (name, description, deadline, expectations, data[0][0]))
        conn.commit()
        print("Post added successfully!")
    except sqlite3.OperationalError:
        print ("not inserted")

def showActivePosts():
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")

    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM internshipposition WHERE deadline >= ? ", [today])
    
    data=cursor.fetchall()
    print("\n")
    for s in data:
        print(s)
    return data

def showCategorisedPosts(id):
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")

    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()

    activePosts = """   SELECT S.nameSoftware, I.name, I.details, I.deadline, I.expectations
                        FROM softwarecompany S
                        INNER JOIN internshipposition I
                        WHERE I.post = S.username AND deadline >= ? AND S.located_in = ?
                  """
    cursor.execute(activePosts, (today, id))
    
    data=cursor.fetchall()
    for s in data:
        print(s)
    return data

def FilteredPostsByKeyword(keyword):
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")

    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()

    activePosts = """   SELECT S.nameSoftware, I.name, I.details, I.deadline, I.expectations
                        FROM internshipposition I 
                        INNER JOIN softwarecompany S
                        WHERE (I.name LIKE ('%' || ? || '%') OR I.details LIKE ('%' || ? || '%') OR I.expectations LIKE ('%' || ? || '%')) 
                               AND I.post = S.username AND deadline >= ?
                  """
    cursor.execute(activePosts, (keyword,keyword,keyword,today))
    
    data=cursor.fetchall()
    for s in data:
        print(s)
    return data

def FilteredPostsByKeywordAndCity(keyword, id):
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")

    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()

    activePosts = """   SELECT S.nameSoftware, I.name, I.details, I.deadline, I.expectations
                        FROM internshipposition I 
                        INNER JOIN softwarecompany S
                        WHERE (I.name LIKE ('%' || ? || '%') OR I.details LIKE ('%' || ? || '%') OR I.expectations LIKE ('%' || ? || '%')) 
                            AND I.post = S.username AND deadline >= ? AND S.located_in = ?
                  """
    cursor.execute(activePosts, (keyword,keyword,keyword,today,id))
    
    data=cursor.fetchall()
    print(data)
    return data

def showallUsers():
    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM softwarecompany")
    
    data=cursor.fetchall()
    for s in data:
        print(s)

def showallPosts():
    conn = sqlite3.connect("my.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM internshipposition")
    
    data=cursor.fetchall()
    for s in data:
        print(s)

# register("alik","salam","KKK","adsd.com","32","aad.com","2","1ad1")
# login("orkhan","salam")
# logOut("132936puz")
# showallUsers()
# postInternship("34002lwi", "HP", "Hedepe poxdu", "Fuck you all", "2021-08-02")
# showallPosts()
# showActivePosts()
# showCategorisedPosts(1)
# FilteredPostsByKeyword("how")
# FilteredPostsByKeywordAndCity("how",1)