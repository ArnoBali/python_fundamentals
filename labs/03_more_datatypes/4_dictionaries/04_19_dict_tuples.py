'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = []

a = input_dict.items()

print(a)

sorted_list = sorted(a, key=lambda x: x[1])

print(sorted_list)