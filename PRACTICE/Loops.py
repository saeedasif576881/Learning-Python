# # while Loop in python 
# no = 1 
# while no <= 3:
#     print("Saeed")
#     no+= 1

# def last(num):
#     if num%2==0:
#         print(num//2)
#         return num//2
#     elif num%2==1:
#         num = (3*num + 1 )
#         print(num)
#         return num

# n = int(input("Enter the no : "))

# while n!=1:
#     n = last(int(n))

# For loop 

# list1 = [1,3,4 ,5, 5,6, 7]

# # for x in list1:
# #     print(x)
    
# for x in range (len(list1)):
#     print(f"Value of {x} index = {list1[x]} ")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
