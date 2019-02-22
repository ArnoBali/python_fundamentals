'''
Take in 10 numbers from the user. Place the numbers in a list.
Calculate the product of all of the numbers in the list.
Also, find the largest number in the list.

Print the results.

'''

'''
i = 3
while True:
    print(i)
    i -= 1
    if i < 1:
        break

print("here")
'''
'''
list_sum = []
i = 3

while i:
    list_sum.append(int(input("Please enter a number :")))
    if i == 0:
        pass #   print("bs") #what to put in here
    else:
        i -= 1
        
print(sum(list_sum))
'''
'''
'''
list_sum = []

for i in range(3):
    list_sum.append(int(input("Please enter a number :")))

print(sum(list_sum))
