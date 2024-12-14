import DataType
import data as dt  # Type alias in python
from data import person1  # When using the from then donot use the data or the file name use the thing you import  
print(DataType.saeed)
dt.greeting("Saeed")
print(dt.person1['country'])
print(person1['age'])
x=dir(dt)
filtered_dt = [attr for attr in x  if not (attr.startswith("__") and attr.endswith("__"))]

print(filtered_dt)