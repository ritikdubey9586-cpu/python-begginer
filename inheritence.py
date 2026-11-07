# Class inheritance allows a new class (known as a child or subclass) to adopt the attributes and methods of an existing class (known as a parent or superclass).
#  This is a foundational concept in Object-Oriented Programming (OOP) that promotes code reusability and prevents you from writing repetitive code.

# Parent Class (Superclass)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f"The {self.brand} {self.model}'s engine is now roaring!"

# Child Class (Subclass) inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        # super() calls the __init__ of the parent class to initialize brand and model
        super().__init__(brand, model)
        # New attribute unique only to Car
        self.doors = doors

    def open_trunk(self):
        return f"Opening the trunk of this {self.doors}-door car."

# ---- Using the Classes ----

# 1. Instantiate the child class
my_car = Car(brand="Tesla", model="Model 3", doors=4)

# 2. Access inherited attributes and methods
print(my_car.brand)          # Output: Tesla
print(my_car.start_engine()) # Output: The Tesla Model 3's engine is now roaring!

# 3. Access child-specific methods
print(my_car.open_trunk())   # Output: Opening the trunk of this 4-door car.
