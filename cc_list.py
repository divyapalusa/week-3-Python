import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while True:
    user = input("Enter to pick a card, or Q then enter to quit :")
    if user == "":

        card = random.choice(diamonds)
        hand.append(card)
        hands_list = diamonds.remove(card)
        print("Your hand :",hand) 
        print("Remaining cards :",diamonds)
    elif user == "Q":
        print("The game is over.")
        exit()
    
    if not diamonds:
        print("There are no more cards to pick.")
