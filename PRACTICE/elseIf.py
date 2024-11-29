# if Else Statement

# Number = int(input("Enter the No you want to check  : "))

# if Number%2==0:
#     print(f"{Number} is even")
# else:
#     print(f"{Number} is odd")
  
# Nested if else   

saeed = 'saeed'

height = int(input("Enter you Height : "))

bill = 0 

if height > 120:
    age = int(input("Enter you Age : "))
    if age <= 12:
        bill = 5
        print("Child can pay 5$")
    elif age<=18:    
        bill = 7
        print("Youth can pay 7$")
    else:
        bill = 12
        print("Adult can pay 12$")
    Take_photo = input("If you want to take photos press y if no press n :")
    if Take_photo=='y':
        print(f"Your final bill is ${bill+3}")
else:
    print("Complain pee ka aa bete")    
    