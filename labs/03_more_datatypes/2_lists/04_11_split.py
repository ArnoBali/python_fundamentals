'''
1. Write a script that takes in a string from the user. Using the split() method,
2.create a list of all the words in the string and
3.print the word with the most occurrences.

'''

string_input = input(str("please add your input here:"))
print(string_input)
#1. Write a script that takes in a string from the user.


list_words = string_input.split()
list_count = []
print(list_words)
#2.create a list of all the words in the string


set_unique = set(list_words)
list_unique = list(set_unique)
print(list_unique)
# create a set that removes all duplicates in list_words

for x in list_unique:
    list_count.append(string_input.count(str(x)))

print(list_count)
# add the counts to list_count

n = max(list_count)

for x in list_unique:
    if string_input.count(str(x)) == n:
        print(x)

#3.print the word with the most occurrences