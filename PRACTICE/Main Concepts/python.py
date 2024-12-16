class Car : 
     
    def __init__(self , name , company, manufacture_date,color,maxSpeed,curent_speed,mileage):
        self.name = name
        self.company = company
        self.__manufacture_date = manufacture_date
        self.color = color
        self.maxSpeed = maxSpeed
        self.curent_speed = curent_speed
        self.mileage = mileage
        
    def start(self):
        print(f"{self.company} {self.name}'s Engine Started!")
        
        self.curent_speed = 0
        
        choices = input("If you want Shift to gear 1 press  Y if not press N ").lower()
        if choices == "y":
            self.gear1()
        elif choices =='n':
            exit()
            
    def gear1(self):
        print(f"{self.company} {self.name} is in gear 1 and the speed is 60" )
        self.curent_speed=60
        self.Accelerate()
    def gear2(self):
        print(f"{self.company} {self.name} is in gear 2 and the speed is 120" )
        self.curent_speed=120
        self.Accelerate()
    def gear3(self):
        print(f"{self.company} {self.name} is in gear 3 and the speed is 180" )
        self.curent_speed=180
        self.Accelerate()
    def gear4(self):
        print(f"{self.company} {self.name} is in gear 4 and the speed is 220" )
        self.curent_speed=220
        self.Accelerate()
        
    def gearshif(self):
        
                choices = str(input(f"You are at speed {self.curent_speed} To Which gear you want to shift for gear 1 press 1, for gear 2 press 2 for gear 3 press 3, for gear 4 press 4 "))
                if choices == "1":
                    self.gear1()
                elif choices=='2':
                    self.gear2()
                elif choices=='3':
                    self.gear3()
                elif choices=='4':
                    self.gear4()
                else :
                    print("Enter a valid choice")
        
    def Accelerate(self):
    
        print(f"Max Speed = {self.maxSpeed}  Current Speed ={self.curent_speed}")
    
        while self.curent_speed <= self.maxSpeed:
            
            if self.curent_speed <= 60:
                choices = input(f"You are at speed {self.curent_speed} Do you want to Shif to gear 2 Press Y if not Press N ").lower()
                if choices == "y":
                    self.gear2()
                elif choices=='n':
                    print(f"car is at a speed of {self.curent_speed} Km/h")
                    self.curent_speed +=30
                else :
                    print("Enter a valid choice")
            if self.curent_speed <= 120:
                choices = input(f"You are at speed {self.curent_speed} Do you want to Shif to gear 3 Press Y if not Press N ").lower()
                if choices == "y":
                    self.gear3()
                elif choices=='n':
                    print(f"car is at a speed of {self.curent_speed} Km/h")
                    self.curent_speed +=30
                else :
                    print("Enter a valid choice")
            if self.curent_speed <= 180:
                choices = input(f"You are at speed {self.curent_speed} Do you want to Shif to gear 4 Press Y if not Press N ").lower()
                if choices == "y":
                    self.gear4()
                elif choices=='n':
                    print(f"car is at a speed of {self.curent_speed} Km/h")
                    self.curent_speed +=30
                else :
                    print("Enter a valid choice")
            
            if self.curent_speed >= 220:
                choices = input(f"You are at speed {self.curent_speed} To which gear  you want to shift press Y for shift and N for remain in the same gear").lower()
                if choices == "y":
                    self.gearshif()
                elif choices=='n':
                    print(f"car is at a speed of {self.curent_speed} Km/h")
                    self.curent_speed +=30
                else :
                    print("Enter a valid choice")
            
            if self.curent_speed>=self.maxSpeed-50:
                choices = input("If you want to Apply Brakes  Press  Y if not Press N ").lower()
                if choices == "y":
                    self.Brake()
                elif choices=='n':
                    print(f"car is at a speed of {self.curent_speed} Km/h")
                    self.curent_speed +=30
                else :
                    print("Enter a valid choice")
            else :
                if self.curent_speed==self.maxSpeed:
                    print(f"You have reached max speed you have to apply brakes else there should be some severe condition")
                else:
                  print(f"car is at a speed of {self.curent_speed} Km/h")
                  self.curent_speed +=30
            continue
                
        print(f"{self.company} {self.name} Reached at max speed of {self.maxSpeed}")
        choices = input("If you Now want to Apply Brakes  Press  Y if not Press N ").lower()
        if choices == "y":
                    self.Brake()
        elif choices=='n':
               self.curent_speed= self.maxSpeed 
               print("You have reach max speed you cannot increase speed from there")
               exit()
        else :
                print("Enter a valid choice")
        
    def Brake(self):
        self.curent_speed = 20
        print(f"Brake applied on {self.company} {self.name} and Speed = {self.curent_speed} Km/h")
        choices = input("If you want to Increase the speed again press  I if you want to Stop  Press S ").lower()
        if choices == "i":
            self.Accelerate()
        elif choices=='s':
            self.Stop()
        else :
            print("Enter a valid choice")
            
            
    def Stop(self):
        self.curent_speed = 0
        print(f"{self.company} {self.name}'s Engine ShutDown!")
        choices = input("If you want to Start Again press  Y if not press N ").lower()
        if choices == "y":
            self.start()
        elif choices=='n':
            exit()
        else :
            print("Enter a valid choice")
        
           
    def detail(self):
        print(f"Company : {self.company} \nName : {self.name}\nManufactured date : {self.__manufacture_date}\nColor : {self.color}\nMileage ={self.mileage}")
    
        
car1 = Car('Cvic','Honda',1998,"white", 340,0,13)
car1.start()



