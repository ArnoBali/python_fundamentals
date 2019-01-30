'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

import math

r = 3.14
h = 5

Surface = (2 * math.pi * r * r) + (2 * math.pi * r * h)
Volume = math.pi * r*r * h

print(Surface)
print(Volume)