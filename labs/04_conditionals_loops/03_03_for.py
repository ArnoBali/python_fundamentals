'''
Using a "for-loop", print out all odd numbers from 1-100.

'''

x = 0

for x in range(100):
    if x % 2 != 0:
        print(x)
    x += 1