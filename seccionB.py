
#set up 
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
password = ""
index = 1

#gathering information  
text = input("Tu texto: ")
original, instructions = text.split(",") 
shift, complement = instructions.split("y") 
complement = [int(x) for x in complement.split() if x.isdigit()]
shift = [int(y) for y in shift.split() if y.isdigit()]


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

#reversing password 
stringlength=len(password) 
finalPassword =password[stringlength::-1] 

#removing "" from input 
finalPassword = finalPassword[1:]
finalPassword = finalPassword[:-1]

#printing final password 
print(finalPassword) 
