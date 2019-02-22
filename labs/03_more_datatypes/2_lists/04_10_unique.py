'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
from typing import Union

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = []

n = list.count

for x in list_:
    if list_.count(x) == 1:
        unique_list.append(x)

print(unique_list)