'''

Write a script that completes the following tasks.

'''

# takes in a number from the user between 1 and 1,000,000,000
x = int(input("input a number between 1 and 1,000,000,000: "))


# calls a function that determines whether the number is divisible by both 4 and 7
def div_and(x):

    if x % 4 == 0 and x % 7 == 0:
        return "Yes, number is divisible by both 4 and 7.."

    else:
        return "No, number isn't divisible by both 4 and 7.."

# calls a function that determines whether the number is divisible by 4 or 7
def div_or(x):

    if x % 4 == 0 or x % 7 == 0:
        return "Yes, number is divisible by 4 or 7.."

    else:
        return "No, number isn't divisible by 4 or 7.."

# calls a function that determines whether the number is divisible by 4 or 7 exclusively
def div_exl(x):

    if (x % 4 == 0 and not x % 7 == 0) or (not x % 4 == 0 and x % 7 == 0): #(a and not b) or (not a and b)
        return "Yes, number is divisible by 4 or 7 exclusively"

    else:
        return "No, number isn't divisible by 4 or 7 exclusively"

# print the results
print(div_and(x))
print(div_or(x))
print(div_exl(x))
