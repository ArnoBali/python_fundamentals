'''
Print out every prime number between 1 and 100.

'''

for x in range(1, 100):
    flag = True
    for y in range(1, x+1):
        if y == x:
            continue
        if y == 1:
            continue
        if x % y == 0:
            flag = False
            break

    if flag == True:
        print(x)

#prime numbers can only be divided by 1 and themselves
