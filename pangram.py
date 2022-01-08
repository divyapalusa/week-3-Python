  
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str:
            return False
  
    return True
      
# Driver code
#string = "the five boxing wizars jumps quickly"
#if(ispangram(string) == True):
    print("True")
#else:
#    print("False")