print(''' 
*******************************************************************************
 ___                                                                  _
/__/|__                                                            __//|
|__|/_/|__                                                       _/_|_||
|_|___|/_/|__                                                 __/_|___||
|___|____|/_/|__                                           __/_|____|_||
|_|___|_____|/_/|_________________________________________/_|_____|___|| 
|___|___|__|___|/__/___/___/___/___/___/___/___/___/___/_|_____|____|_||
|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___||
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_||
|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/
*********************************************************************************
''')

print("Welcome to Treasure Island \n Your mission is to find the treasure")
name = input("Enter you Name : ")
print("You are at a cross road. Where do you want to go?")
user_input = input("Type l for left and r for Right :").lower()

if user_input == 'l':
    user_input1 = input(f"{name} You've come to the lake. There is an island in the middle of the lake\n Type w for wait for the boat or type s for swiming across.  ").lower()

    if user_input1 == 'w':
        user_input2= input(f"{name} You arrive at the island unharmed There is a house with 3 doors.\n One red (r), one yellow (y), and one blue(b),. which color do you choose? ").lower()

        if user_input2 == 'y' :
            print(f"Hurrah {name} You Won the Game"+ '''
__   __           __        __          
\ \ / /__  _   _  \ \      / /__  _ __  
 \ V / _ \| | | |  \ \ /\ / / _ \| '_ \ 
  | | (_) | |_| |   \ V  V / (_) | | | |
  |_|\___/ \__,_|    \_/\_/ \___/|_| |_|''' +     '''
                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=- 
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.' 
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  * 
  '..'  ':::'     * /\ *     .'/.\'.   ' 
      *            *..*         : 
     * 
        *''')
        elif user_input2 == 'b' or user_input2 == 'B': 
            print(f"{name} you entered the room of beast and Game Over"+ 
                  """
  _____                         ____        
 / ____|                       / __ \                
| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| 
| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
 \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                     """ )
        elif user_input2 == 'r' or user_input2 == 'r': 
            print(f"{name} you entered the room of fire and Game Over" + 
                  """
  _____                         ____        
 / ____|                       / __ \                
| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| 
| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
 \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                     """ )
        else:
            print("Invalid Choice")
    elif user_input1 == 's':
        print(f"{name} You Got attacked by shark  and Game Over" + 
                  """
  _____                         ____        
 / ____|                       / __ \                
| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| 
| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
 \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                     """ )
    else:
        print("Invalid Choice")
elif user_input=='r':
    print(f"{name} You fell in a hole and Game Over"+ 
                  """
  _____                         ____        
 / ____|                       / __ \                
| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| 
| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
 \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                     """ )
else:
    print("Invalid Choice")
