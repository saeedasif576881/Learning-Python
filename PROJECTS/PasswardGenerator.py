import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
                      '[', ']', '{', '}', '|', ':', ';', '"', "'", '<', '>', ',', '.', 
                      '/', '?', '~', '`']
lowercase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

passward = [numbers,special_characters,lowercase_alphabets,uppercase_alphabets]
print('Welcome to the PyPassword Generator!')

Uppercase = int(input("How many Uppercase Alphabets would you like in your password? \n"))
pasward_list = random.choices(uppercase_alphabets,k=Uppercase)

Lowercase = int(input("How many Lowercase Alphabets would you like in your password? \n"))
pasward_list.extend(random.choices(lowercase_alphabets,k=Lowercase))
Numbers = int(input("How many Numbers would you like in your password? \n"))
pasward_list.extend(random.choices(numbers,k=Numbers))
Special_Char = int(input("How many Special Characters would you like in your password? \n"))
pasward_list.extend(random.choices(special_characters,k=Special_Char))
print(pasward_list)
random.shuffle(pasward_list)
print(pasward_list)
Final_passward = ' '.join(pasward_list)
print(f'Your Passward is : {Final_passward}')


