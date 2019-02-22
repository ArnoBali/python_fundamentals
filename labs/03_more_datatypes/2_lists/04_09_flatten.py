'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

list1 = [1, 2, 3, 4]
list2 = [5, 6]
list3 = [7, 8, 9]
list4= []

flat_list= []

list4.append(list1)
list4.append(list2)
list4.append(list3)

print(list4)
#print(sum(list4, []))

for sublist in list4:
    for item in sublist:
        flat_list.append(item)

print(flat_list)