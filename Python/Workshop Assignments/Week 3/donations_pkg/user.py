def login(database, username, password):
    if username in database.keys():
        if password == database[username]:
            print ("Welcome back, " + username + "!")
            return username
    if username in database.keys():
        if password != database[username]:
            print("Incorrect password for" + username)
            return ""
    if username not in database and password not in database:
        print("Unknown username and password!")
        return ""

def register(database, username):
    if username in database.keys():
        print ("Username already registered!")
        return ""
    if username not in database:
        print(username + " has been registered")
        return username