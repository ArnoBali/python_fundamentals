'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

input1 = input(str("please add your text here:"))
#user input


input1_list = list(input1)
print(input1_list)

dict = {}

for i in input1_list:
    dict[i] = input1_list.count(i)

print(dict)