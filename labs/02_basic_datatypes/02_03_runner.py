'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

miles = 10
minutes = 30
seconds = 30
km = miles * 1.6

sec2min = seconds / 60

hour = (minutes + sec2min) / 60

avSpeed = km / hour

print(avSpeed)