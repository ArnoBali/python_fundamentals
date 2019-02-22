'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''
a = int(input("please enter a lower bound:"))
b = int(input("please enter a upper bound:"))


x = a
list1 = []
for x in range(a, b+1):
    list1.append(x)
    x += 1

result = sum(list1)

print(result)
