state_capitals = {"Washington": "Olympia", "Oregon": "Salem", "California": "Sacramento"}
#print(len(state_capitals))
# Accesing values
#print(state_capitals["Washington"])
state_capitals["Washington"] = "Aberdeen"
state_capitals["Texas"] = "Austin" # Insert new key value pair
print(state_capitals)
del state_capitals["California"] # deleting key word using DEL
print(state_capitals)
removed_capital = state_capitals.pop("Oregon") # deleting key word using POP
print(state_capitals)
print(removed_capital)
