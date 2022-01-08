from donations_pkg.homepage import show_homepage,donate,show_donations
from donations_pkg.user import login,register
database = {"admin":"password123"}
donations = []
authorized_user = " "
#main program
show_homepage()
if authorized_user == " ":
    print("You must be logged in to donate.")
else:
    print("Logged in as :" ,authorized_user)

while True:

    show_homepage()
    user = input("choose an option : ")


    if user =="1":
        username = input("Enter username :")
        password = input("Enter password :")   
        #print("TODO : Write Login Functionality.")
        authorized_user = login(database,username,password)
        

    
        

    elif user =="2":
        username = input("Enter username :")
        password = input("Enter password :")
        
        #print("TODO :  Write Register Functionality.")
        authorized_user = register(database,username)
        database[authorized_user] = password
        
        
    elif user == "3":
        username = input("Enter username :")
        password = input("Enter password :")
        
    
        if authorized_user == " ":
           print("you are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
            #print(username ,"donated "+" $ " + "{}".format(donation))
            print("Thank you for your donation!")
        
    elif user =="4":
     
        show_donations(donations)
        #donations.append(authorized_user , "donated $" + "{}".format(donation))
        #print(username ,"donated $" + "{}".format(donation))
        
        #print(username ,donation)
    elif user =="5":
        print("Leaving DonateMe...") 
        break
    else:
        print("In valid option ,try again .")
        
        


