'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

#1)
float(1)

#2)
int(1.444)

#3)
1.05 // 2

#4)

input1 = float(input("Please enter a number between 1 and 1,000,000,000: "))
input2 = float(input("Please enter a number between 1 and 1,000,000,000: "))

multi = input1 * input2

print(multi)