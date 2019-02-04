'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

string1 = input("Please enter your 1st message: ")
string2 = input("Please enter your 2nd message: ")
string3 = input("Please enter your 3rd message: ")

len1 = len(string1)
len2 = len(string2)
len3 = len(string3)

if(len1 > len2) and (len1 > len3):
    print(string1)
elif(len2 > len1) and (len2 > len3):
    print(string2)
elif(len3 > len1) and (len3 > len2):
    print(string3)

else:
    print("nice try")