import random



rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
obj = [rock,paper,Scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice >= 3  or user_choice<0:  
    print("Invalid Choice ! Computer Won")
else :
    
    computer_Choice = random.randint(0,2)
    print(f"{user_choice}\n{obj[user_choice]}")
    print(f"{computer_Choice}\n{obj[computer_Choice]}")

    if computer_Choice== user_choice:
     print("Match Draw" )
    elif computer_Choice==0 and user_choice==1:
     print("User Won" )
    elif computer_Choice==0 and user_choice==2:
     print("Computer Won" )
    elif computer_Choice==1 and user_choice==0:
     print("Computer Won" )
    elif computer_Choice==1 and user_choice==2:
     print(f"{user_choice}\n {Scissors}  computer Choice : {computer_Choice}\n {paper} User Won" )
    elif computer_Choice==2 and user_choice==0:
     print("User Won" )
    elif  computer_Choice==1 and user_choice==2:
      print("Computer Draw" )



    



