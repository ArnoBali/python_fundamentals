'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_rectangle(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area_circle(self):
        return (self.radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self.radius

i_rectangle = Rectangle(4, 5)
i_circle = Circle(10)

print(i_rectangle.area_rectangle())
print(i_rectangle.perimeter())
print(i_circle.area_circle())
print(i_circle.circumference())