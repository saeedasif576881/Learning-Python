class Person:
    family = 'Arain'
    def __init__(self, age ,height=None, name=None ):
        self.name= name
        self.age = age
        self.height = height 
        
        
        
    def sound(self,sound ):
        print( f"My Name is {sound}")
    def introduction(self):
        return f"My name is {self.name} and my age is {self.age}"        
        
        
        
        
obj1 = Person(12,122,'waheed')

print(obj1.age)
print(obj1.height)
print(obj1.family)
intro = obj1.introduction()
print(intro)
obj1.sound("Meao Meao")


