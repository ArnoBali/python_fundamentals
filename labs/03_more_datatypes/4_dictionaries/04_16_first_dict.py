'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''



n = [1,2,3,4,5,6,7,8,9,10]
dict = {}

for i in n:
    dict[i] = i*i

print(dict)

