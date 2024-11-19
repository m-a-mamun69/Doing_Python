
# --- Python Class.

class Car:
    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"{self.brand} {self.model} has {self.wheels} Whells.")


car1 = Car("BMW", "7-Series")
car2 = Car("Mercedes", "S-Class")

car1.display_info()
car2.display_info()