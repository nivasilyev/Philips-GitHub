import random, sys

Instructions = """

There are 13 coins.  2 Players take turns taking coins until the last person takes the last coin.
That person loses.  
You can only take 1, 2, or 3 coins on your turn.

"""

print(Instructions)
number = 13
listYes = ["YES", "YE", "Y", "SURE"]
listNo = ["NO", "N"]


#Do you want to go first?
def playAgain():
    global number
    options = "[Y]ES [N]O\n"
    while True:
        if number == 0:
            prettyFormat = "Do you want to play again?\n" + options
        else:
            prettyFormat = "Do you want to play?\n" + options
        playAGame = input(prettyFormat)
        if playAGame.upper() in listNo:
            anotherGame = False
            sys.exit()
            return (anotherGame, False)
        if playAGame.upper() in listYes:
            anotherGame = True
            number = 13
            while True:
                firstTurn = input('Do you want to go first?\n' + options)
                if firstTurn.upper() in listYes:
                    goFirst = True
                    return (anotherGame, goFirst)
                elif firstTurn.upper() in listNo:
                    goFirst = False
                    return (anotherGame, goFirst)
            else: 
                print("I'm not familiar with that.")
                
    return (anotherGame, goFirst)


#Check current number

    
#Prompt user to take 1-3 coins
while True:
    if number == 0 or number == 13:
        play = playAgain()
        game = play[0]
        goFirst = play[1]   

    print()

#If goFirst == False Take 2 Coins
    if goFirst == False and number==13:
        print("Then I will go first, ", end ="")
        opponent = random.randint(1, 3)
        number -= opponent
        if opponent == 1:
            print("I take 1 coin.  Your Turn.")
        else:
            print("I take " + str(opponent) + " coins.  Your Turn.")
# if number > 1 and number <13
            
            
    if number == 1:
        print("There is 1 coin.")
    else:
        print('There are ' + str(number) + ' coins.')
    print('How many do you take?')
    if number == 1:
        options = "[1]\n"
    elif number == 2:
        options = "[1] [2]\n"
    else:
        options = "[1] [2] [3]\n"
    while True:
        take = input(options)
        if (take == "break") or (take == "quit"):
            number = 0
            sys.exit()
        if take.isnumeric():
            if 1<=int(take) and int(take)<=3:
                number = number-int(take)
                print()
                break    
            else:
                print('Take between one and three\n' + str(number) + ' coins remain.')
# Other player goes
# Win Condition
    if number == 0:
        print("You lost, try harder next time.")
        continue
#    print("There are " + str(number) + " coins.")
    if number == 1:
        playAgain = input("There is 1 coin. \nI lost.")
        number = 0
        continue
#Save the Wins and Losses for User
    print(str(number) + " coins.")
    print("You took "+ take + " coins. ", end = "")    
    if number%4 == 1:
        opponent = random.randint(1, 3)
        number -= opponent
        if opponent == 1:
                print("I take " + str(opponent) + " coin.  Your Turn.")
                continue
        else:
            print("I take " + str(opponent) + " coins.  Your Turn.")
            continue
    if number%4 == 2:
        number -= 1
        print("I take 1 coin.  Your Turn.")
        continue
    if number%4 == 3:
        number -= 2
        print("I take 2 coins.  Your Turn.")
        continue
    if number%4 == 0:
        number -= 3
        print("I take 3 coins.  Your Turn.")
        continue




            