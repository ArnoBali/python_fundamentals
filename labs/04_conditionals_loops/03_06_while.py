'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''
x = 1

while x <= 100:
    if x % 5 == 0:
        print(x)
    x += 1
