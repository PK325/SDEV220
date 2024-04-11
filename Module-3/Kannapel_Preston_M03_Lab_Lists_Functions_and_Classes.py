# Created by : Preston Kannapel
# File Name : Kannapel_Preston_M03_Lab_Lists_Functions_and_Classes
# Date : 4/7/2024
# Assignment : M03 Lab - Case Study: Lists, Functions, and Classes
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():
    # User inputs Vehicle Information
    vehicle_type = "car"
    year = input("Enter the Vehicle's year: ")
    make = input("Enter the Vehicle's make: ")
    model = input("Enter the Vehicle's model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Creates an Automobile object with the information
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    # Outputs all vehicle data
    print(f"Vehicle type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")

if __name__ == "__main__":
    main()
