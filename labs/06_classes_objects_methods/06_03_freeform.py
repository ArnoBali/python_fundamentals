'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''


class Plate:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.amount = 4

    def plate_attributes(self):
        return f"List of a plates's attributes: {self.shape}, {self.color}, {self.amount}."

    def __str__(self):
        return  f"List of a plates's attributes: {self.shape}, {self.color}, {self.amount}."


class Cup:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.amount = 2

    def cup_attributes(self):
        return f"List of a cup's attributes: {self.shape}, {self.color}, {self.amount}."

    def __str__(self):
        return f"List of a cup's attributes: {self.shape}, {self.color}, {self.amount}."

class Flower:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.amount = 22

    def flower_attributes(self):
        return f"List of a flower's attributes: {self.shape}, {self.color}, {self.amount}."

    def __str__(self):
        return f"List of a flower's attributes: {self.shape}, {self.color}, {self.amount}."


plate1 = Plate('round', 'blue')
plate2 = Plate('square', 'green')
cup1 = Cup('bulky','pimple')
cup2 = Cup('flat', 'transparent')
flower1 = Flower('tall', 'white')
flower2 = Flower('bendy', 'red')

plate1.color = "pink"
cup1.color = "pink"
flower1.color = "pink"

print(plate1.plate_attributes())
print(plate2.plate_attributes())
print(plate1)

print(cup1.cup_attributes())
print(cup2.cup_attributes())
print(cup2)

print(flower1.flower_attributes())
print(flower2.flower_attributes())
print(flower2)


