
def show_homepage():
    print("")

    print("      === DonateMe Homepage ===   ")
    print("---------------------------------------")
    print("| 1.   Login    | 2.   Register        |")
    print("---------------------------------------")
    print("| 3.   Donate   | 4.   Show Donations  |")
    print("---------------------------------------")
    print("|            5. Exit                   |")
    print("---------------------------------------")
    
def donate(username):
    donation_amt = float(input("Enter amount to donate :"))
    donation = username  +  " donated $ " +str(donation_amt)
    return  donation
def show_donations(donations):
    print("------ All Donations-------")
    
    if donations == []:
        print("currently, there are no donations. ")
    else:
        
        for donation in donations:
            print(donation)
            #print( username,donation)
            #print( username ,"donated $ ",str(donation))
    
