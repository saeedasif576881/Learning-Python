# All the thing in Python are treated like an object

a = complex(3,4)
print(a) 
print(type(a))

# Lists are the list of objects, data , and list also include the list

list = ["saeed",1 , "Waheed"]
print(list)

# Tupples are immutable

tupple1 = ("saeed",12 , "waheed");
print(tupple1)

# Dictionary (dist) it stores key value pairs
# There are no duplicate values in dist


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))

dist = {
    'Name':'saeed',
    'Age' :22

}

print(dist)



a = input("Enter the first No : ")
b = input("Enter the Second No : ")

a = int(a)
b = int(b)

print(a+b)