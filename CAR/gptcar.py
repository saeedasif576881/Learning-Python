class Car:
    def __init__(self, name, company, manufacture_date, color, max_speed, current_speed, mileage):
        self.name = name
        self.company = company
        self.__manufacture_date = manufacture_date
        self.color = color
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.mileage = mileage

    def start(self):
        print(f"{self.company} {self.name}'s Engine Started!")
        self.current_speed = 0
        self.accelerate()

    def shift_gear(self, gear):
        speeds = {1: 60, 2: 120, 3: 180, 4: 220}
        if gear in speeds:
            self.current_speed = speeds[gear]
            print(f"{self.company} {self.name} is now in gear {gear} at speed {self.current_speed} km/h.")
        else:
            print("Invalid gear choice!")

    def accelerate(self):
        while self.current_speed < self.max_speed:
            print(f"Current Speed: {self.current_speed} km/h. Max Speed: {self.max_speed} km/h.")

            # Gear selection
            if self.current_speed < 220:  # Below Gear 4 speed
                try:
                    gear = int(input("Enter the gear (1-4) you want to shift to, or 0 to apply brakes: "))
                    if gear == 0:
                        self.brake()
                        return
                    elif 1 <= gear <= 4:
                        self.shift_gear(gear)
                    else:
                        print("Invalid gear choice!")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                # After reaching Gear 4, allow speed to increase in increments of 30
                increase_speed = input("Do you want to increase speed further? (Y/N): ").lower()
                if increase_speed == 'y':
                    if self.current_speed + 30 <= self.max_speed:
                        self.current_speed += 30
                        print(f"Speed increased to {self.current_speed} km/h.")
                    else:
                        print(f"You've reached the maximum speed: {self.max_speed} km/h.")
                        break
                elif increase_speed == 'n':
                    print(f"Maintaining speed at {self.current_speed} km/h.")
                else:
                    print("Invalid choice.")

        print(f"{self.company} {self.name} has reached the maximum speed of {self.max_speed} km/h.")
        self.brake()

    def brake(self):
        print(f"Brake applied! {self.company} {self.name} is slowing down.")
        self.current_speed = 0
        self.stop()

    def stop(self):
        print(f"{self.company} {self.name}'s Engine Shut Down.")
        restart = input("Do you want to restart the car? (Y/N): ").lower()
        if restart == 'y':
            self.start()
        else:
            print("Car stopped.")

    def details(self):
        print(f"""
        Car Details:
        Company: {self.company}
        Name: {self.name}
        Manufacture Date: {self.__manufacture_date}
        Color: {self.color}
        Mileage: {self.mileage} km/l
        """)


# Example usage
car1 = Car('Civic', 'Honda', 1998, "White", 340, 0, 13)
car1.start()
