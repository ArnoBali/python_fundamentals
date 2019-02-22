'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

input1 = input(str("please add your input here:"))
print(input1)


word = input1.split()
print(word)
result_list = []


for x in word:
    result_list.append(tuple(str(x)))


print(result_list)

