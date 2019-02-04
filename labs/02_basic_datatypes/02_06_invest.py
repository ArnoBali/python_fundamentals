'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

investment = float(input("Please enter the investment amount: "))
interestRate = float(input("Please enter the interest rate (in percentage): "))
years = float(input("Please enter the number of years to invest: "))

futureValue = investment * ((1 + interestRate / 100) ** years)
print(futureValue)