'''
Print out every prime number between 1 and 100.

'''

x = 0
y = 0

for x in range(100):
    if lambda y: x % y != 0:
        print(x)
    x += 1

#prime numbers can only be devided by 1 and themselves
#not finished!!!