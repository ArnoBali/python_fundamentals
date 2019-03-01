'''
Build on the previous exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercise.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.wheels = 4

    def vehicle_attributes(self):
        return f"List of a vehicle's attributes: {self.brand}, {self.color}, {self.wheels}."

    def __str__(self):
        return  f"List of a vehicle's attributes: {self.brand}, {self.color}, {self.wheels}."


class Car(Vehicle):
    def __init__(self, brand, color, speed):
        super().__init__(brand, color)
        self.speed = speed

    def car_attributes(self):
        return f"List of a car's attributes: {self.brand}, {self.color}, {self.wheels}, {self.speed}."

    def __str__(self):
        return  f"List of a car's attributes: {self.brand}, {self.color}, {self.wheels}, {self.speed}."



class Car_age(Car):
    def __init__(self, brand, color, speed, year):
        super().__init__(brand, color, speed)
        self.year = year

    def car_age_attributes(self):
        return f"List of a car's attributes: {self.brand}, {self.color}, {self.wheels}, {self.speed}, {self.year}."


    def __str__(self):
        return f"List of a car's attributes: {self.brand}, {self.color}, {self.wheels}, {self.speed}, {self.year}."


vehicle1 = Vehicle('audi', 'blue')
vehicle2 = Vehicle('ferrari', 'red')
car1 = Car('audi', 'blue', '140 km/h')
car2 = Car('ferrari', 'red', '200 km/h')
car_age1 = Car_age('bmw', 'pink', '30 km/h', 1970)
car_age2 = Car_age('jag', 'yellow', '300 km/h', 2020)

print(vehicle1)
print(car1)
print(car_age1)