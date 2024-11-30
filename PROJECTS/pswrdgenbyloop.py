import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
                      '[', ']', '{', '}', '|', ':', ';', '"', "'", '<', '>', ',', '.', 
                      '/', '?', '~', '`']
lowercase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print('Welcome to the PyPassword Generator!')
Uppercase = int(input("How many Uppercase Alphabets would you like in your password? \n"))
Lowercase = int(input("How many Lowercase Alphabets would you like in your password? \n"))
Numbers = int(input("How many Numbers would you like in your password? \n"))
Special_Char = int(input("How many Special Characters would you like in your password? \n"))
passward= []
for x in range (Uppercase):
    passward.append(random.choice(uppercase_alphabets))
    
for x in range (Lowercase):
    passward.append(random.choice(lowercase_alphabets))
   
for x in range (Numbers):
    passward.append(random.choice(numbers))
    
for x in range (Special_Char):
    passward.append(random.choice(special_characters))
    
print(passward)   
random.shuffle(passward)
print(passward)

Final_pas = ''.join(passward)
print(f"Your Final Passward is: {Final_pas}")
