class Vehicle:
    def __init__(self, color, current_speed=0):
        self.color = color
        self.current_speed = current_speed

    def start(self):
        print("Vehicle engine started!")
        self.current_speed = 0

    def brake(self):
        self.current_speed = 0
        print("Vehicle has stopped.")

    def stop(self):
        print("Vehicle engine shut down.")

    def details(self):
        print(f"Vehicle Color: {self.color}\nCurrent Speed: {self.current_speed} km/h")


class Car(Vehicle):
    def __init__(self, name, company, manufacture_date, color, max_speed, mileage):
        super().__init__(color)
        self.name = name
        self.company = company
        self.__manufacture_date = manufacture_date
        self.max_speed = max_speed
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
                increase_speed = input("Do you want to increase speed further? (Y/N): ").strip().lower()
                if increase_speed == 'y' and self.current_speed + 30 <= self.max_speed:
                    self.current_speed += 30
                    print(f"Speed increased to {self.current_speed} km/h.")
                elif increase_speed == 'n':
                    print(f"Maintaining speed at {self.current_speed} km/h.")
                    return  # Exit the loop to stop accelerating further
                else:
                    print("Invalid choice or maximum speed reached.")

        if self.current_speed == self.max_speed:
            print(f"{self.company} {self.name} has reached the maximum speed of {self.max_speed} km/h.")
        self.brake()

    def brake(self):
        print(f"Brake applied! {self.company} {self.name} is slowing down.")
        self.current_speed = 0
        self.stop()

    def stop(self):
        print(f"{self.company} {self.name}'s Engine Shut Down.")
        restart = input("Do you want to restart the car? (Y/N): ").strip().lower()
        if restart == 'y':
            self.start()
        else:
            print("Car stopped.")

    def details(self):
        print(f"""
        Vehicle Details:
        Company: {self.company}
        Name: {self.name}
        Color: {self.color}
        Current Speed: {self.current_speed} km/h
        Manufacture Date: {self.__manufacture_date}
        Mileage: {self.mileage} km/l
        Max Speed: {self.max_speed} km/h
        """)


# Example usage
if __name__ == "__main__":
    car1 = Car('Civic', 'Honda', 1998, "White", 340, 13)
    car1.start()
    car1.details()
