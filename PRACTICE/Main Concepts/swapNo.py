# Function to swap two numbers
# from enum import Enum

# class Role (Enum):
#     Admin = 1 
#     User = 2

def swap_numbers(a, b):
    return b, a

# Main program
def main():
    print("Welcome to the Swap Program!")
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))
    
    swaps = 0
    limit = 2
    
    personRole = input("Enter your Role if Admin press A and if User press u").strip().lower()

    while swaps < limit    :
        
        if personRole== 'a':
            limit = 1000 
        elif personRole== 'u':
            limit=2
        else:
            print("Enter a Valid Choice ??")    
        
        print(f"\nBefore swap {swaps + 1}: a = {a}, b = {b}")
        
        # Ask the user if they want to swap
        proceed = input("Do you want to swap the numbers? (yes/no): ").strip().lower()
        if proceed != "yes":
            print("Exiting the program.")
            return
        
        # Perform the swap
        a, b = swap_numbers(a, b)
        swaps += 1
        print(f"After swap {swaps}: a = {a}, b = {b}")

    print("\nYou have reached the swap limit. No more swaps allowed!")
   

# Run the program
if __name__ == "__main__":
    main()
