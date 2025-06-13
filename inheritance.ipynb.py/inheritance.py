# inheritance.ipynb
# Parent class
class Vehicle:
    def move(self):
        print("The vehicle is moving")
        
        # Child class
class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

# Using the child class
my_car = Car()
my_car.move()
my_car.honk()

# Parent class
class Employee:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Employee Name: {self.name}")

        # Child class
class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def show_info(self):
        print(f"Manager Name: {self.name}, Department: {self.department}")

mgr = Manager("Alice", "Sales")
mgr.show_info()