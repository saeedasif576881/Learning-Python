print("Welcome to the tip Calculator!")
t_bill= float(input("What was the total bill? $"))
tip = int(input("How much tip do you like to give ? 10, 12 or 15? "))
people= int(input("How many people to split the bill? "))


t_bill = (t_bill * (1 + tip/100))/people;
t_bill = round(t_bill,2)
# Both are the way of printing the formated data and in the second one you donot have to typecast the value
# 1-print("Each Person should pay: $" + str(t_bill))
print(f"Each Person should pay: ${t_bill}")