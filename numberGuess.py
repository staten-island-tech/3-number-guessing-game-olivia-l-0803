


import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
randomNumber = random.choice(list)

userGuess = int(input("Guess a number between 1 and 10 :-) "))
guessed = False

while not guessed:
    if userGuess == randomNumber:
        print("You guessed it right! WOw!!!!")
        guessed = True
    elif userGuess < randomNumber:
        userGuess = int(input("Too low, try again "))
    elif userGuess > randomNumber:
        userGuess = int(input("Too high, try again "))
