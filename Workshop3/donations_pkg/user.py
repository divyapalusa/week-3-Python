def login(database, username,password):
    #database = {"username":"password"}
    # if username in database and password== database[username]:
    #     print("Welcome back","{}".format(username))
    #     print("Logged in as :",username)
    #     return username
    # elif username in database and password != database[username]:
    #     print("Incorrect password for",username)
    #     return " "

    # else:
    #     print("User not found. Please Register.")
    #     return " "
    
    if username in database:

        if password == database[username]:
            print("Welcome back","{}!".format(username))
            print("Logged in as :",username)
            return username
        print("Incorrect password.")
        return " "
    return " "

        
    

def register(database,username):
    if username in database:
        print(username, "has already registerd.")
        return 
    else:
        print(username," has been registerd.")
    return username



