'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

string = input("Please enter your message: ")

symbol = input("Please enter your symbol: ")

targetCharacter = string[0]

newString = string\
    .replace(targetCharacter.upper(), symbol)\
    .replace(targetCharacter.lower(), symbol)

print(newString)

