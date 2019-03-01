'''
Code a game of rock paper scissors.

'''



# function to get hand based on number
# the function should take in a number and return the string representation of the hand
def get_hand(input):
    # 0 = scissor, 1 = rock, 2 = paper
    if input == 0:
        return 'scissor'
    elif input == 1:
        return 'rock'
    elif input == 2:
        return 'paper'

    # for example if the variable hand is 0, it should return the string "scissor"
    pass

# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(hand_user, hand_comp):
    if hand_user == 0 and hand_comp == 0:
        return "Tie, please try again"
    elif hand_user == 0 and hand_comp == 1:
        return "You lose"
    elif hand_user == 0 and hand_comp == 2:
        return "Winning!"
    elif hand_user == 1 and hand_comp == 0:
        return "Winning"
    elif hand_user == 1 and hand_comp == 1:
        return "Tie, please try again"
    elif hand_user == 1 and hand_comp == 2:
        return "You lose"
    elif hand_user == 2 and hand_comp == 0:
        return "You lose"
    elif hand_user == 2 and hand_comp == 1:
        return "Winning"
    elif hand_user == 2 and hand_comp == 2:
        return "Tie, please try again"

    pass

'''
Start here
'''

while True:
    # take in a number 0-2 from the user that represents their hand
    hand_user = int(input("Please input a number between 0-2: "))

    # generate a random number 0-2 to use for the computer's hand
    import random
    hand_comp = random.randint(0,2)

    # call the function get_hand to get the string representation of the user's hand
    print(f"user: {get_hand(hand_user)}")

    # call the function get_hand to get the string representation of the computer's hand
    print(f"comp: {get_hand(hand_comp)}")


    # call the function determine_winner to figure out the winner
    print(determine_winner(hand_user,hand_comp))

    if determine_winner(hand_user,hand_comp) != "Tie, please try again":
        break

# print out the player hand and computer hand
print(f"{get_hand(hand_user)}-{get_hand(hand_comp)}")
# print out the winner

