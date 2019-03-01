'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase_max_speed(self):
        self.max_speed += 5

    def details_car(self):
        return f"Car details: {self.model}, {self.year}, {self.max_speed}"

i1 = Car("audi R3", "2017", "212 km/h")
i2 = Car("telsa model 3", "2019", "250 km/h")

i2.max_speed = 200

print(i2.details_car())