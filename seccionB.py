
#gathering information  
text = input("Tu texto: ")
#gathering input  
try:  #if complement and shift are specified 
    original, instructions = text.split(",") 
    shift, complement = instructions.split("y") 
    complement = [int(x) for x in complement.split() if x.isdigit()]
    shift = [int(y) for y in shift.split() if y.isdigit()]
except ValueError: #if complement and shift are not specified 
    original = text
    shift = [3]
    complement = [9]

#function to encrypt password
def encrypt(original, shift, complement):
    #set up 
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    password = ""
    index = 1
    for elements in original:  #looping through string using index
        try: #for letter characters  
            newCharacter = alphabet[alphabet.index(elements.lower()) + shift[0]] #shifting through alphabet 
            if index % 2 == 0: newCharacter = newCharacter.upper() #uppercase even numbers
        except ValueError:
            try:
                newCharacter = str(complement[0] - int(elements)) #compliment of integers
            except ValueError:
                newCharacter = elements  #other characters stay the same
        index = index + 1
        password = password + newCharacter  #adding to new password  
    return password  

#reversing password 
password = encrypt(original, shift, complement)
stringlength=len(password) 
finalPassword =password[stringlength::-1] 

#removing "" from input if neccesary 
if finalPassword[0] == "\"" and finalPassword[-1] == "\"": 
    finalPassword = finalPassword[1:]
    finalPassword = finalPassword[:-1]

#printing final password 
print(finalPassword) 



