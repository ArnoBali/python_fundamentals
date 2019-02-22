'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

a = int(input("please enter a number between 1-12:"))

if a == 1:
    print("January")
elif a == 2:
    print("February")
elif a == 3:
    print("March")
elif a == 4:
    print("April")
elif a == 5:
    print("May")
elif a == 6:
    print("June")
elif a == 7:
    print("July")
elif a == 8:
    print("August")
elif a == 9:
    print("September")
elif a == 10:
    print("October")
elif a == 11:
    print("November")
elif a == 12:
    print("December")
else:
    print("other")
