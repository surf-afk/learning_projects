## this will be a number guessing game where the user will guess a number between 1-100. 

import random

##simple function to remove all spaces and make a sting lower case.
def remove_spaces_and_caps(text):
    text_no_white_space = text.replace(" ", "")
    return text_no_white_space.lower()

## define the bounds for the guessing game
## set the bounds to be further appart the harder the difficultly the user selects.

## get the users desiered difficulty
difficulty = input("How hard to you want the number guessing game to be? \n easy, medium, or hard?")
difficulty = remove_spaces_and_caps(difficulty)

## logic to set bounds based on users difficulty selection
if difficulty == "hard":
    lowerBound = 1
    upperBound = 100
elif difficulty == "medium":
    lowerBound = 1
    upperBound = 25
elif difficulty == "easy":
    lowerBound = 1
    upperBound = 10

## generate the random integer for the user to guess.
randInt = random.randint(lowerBound,upperBound)

## Get the guess from the user
userGuess = int(input("Guess the number:"))

## Logic code for comparing user imput to the random number
## the user gets three guesses to find the number with hints about which dirrection they need to change theur guess.
for i in range(3):
    if userGuess != randInt and i == 2:
        print("Sorry wrong again and you ran out of guesses. Better luck next time")
        break
    elif userGuess > randInt: 
        print(f"You guessed too high. Try again! \n You have {2-i} guesses left.")
        userGuess = int(input("Guess again:"))
    elif userGuess < randInt:
        print(f"You guessed too low. Try again! \n You have {2-i} guesses left.")
        userGuess = int(input("Guess again:"))
    else:
        print("Congradualtions you guessed right!")
        break