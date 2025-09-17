import random 

 
randomNumber = random.randint(1, 10)
guessed = False

print("Hi! Lets play a number guessing game :-] ")
YourAnswer = int(input("Guess a number from 1 - 10: "))

while not guessed:
    if YourAnswer == randomNumber:
        print("Nice! You got it right!")
        guessed = True
    elif YourAnswer > randomNumber:
        YourAnswer = int(input("Sorry, that's too high. Try again? "))
    elif YourAnswer < randomNumber:
        YourAnswer = int(input("Sorry, that's too low. Try again? "))

print("Lets go to level 2!")

randomNumber = random.randint(1, 30)
guessed = False

YourAnswer = int(input("Guess a number from 1-30: "))

while not guessed: 
    if YourAnswer == randomNumber:
        print("Yay! You got it again.")
        guessed = True
    elif YourAnswer > randomNumber:
        YourAnswer = int(input("That's too high! Try again? "))
    elif YourAnswer < randomNumber:
        YourAnswer = int(input("That's too low! Try again? "))

print("You're good at this! Try level 3 :-D")


randomNumber = random.randint(1, 50)
guessed = False

YourAnswer = int(input("Guess!"))

while not guessed:
    if YourAnswer == randomNumber:
        print("Wow! You did it!")
        guessed = True
    elif abs(randomNumber - YourAnswer) <= 2:
        YourAnswer = int(input("Very warm!! Try again: "))
    elif abs(randomNumber - YourAnswer) <= 5:
        YourAnswer = int(input("Warm! Try again? "))
    elif abs(randomNumber - YourAnswer) <= 8:
        YourAnswer = int(input("Cooler, try again? "))
    else:
        YourAnswer = int(input("Cold... try again.. "))

print("Yay!!! You completed the game!! You will get FREE private tickets to the turtle show! :-P")

import turtle
turtle.shape("turtle")

def star(length):
    for i in range(5):
        turtle.forward(length)
        turtle.right(144)

def starspiral(length, iterate):
    for i in range(iterate):
        star(length)
        turtle.right(5)
        length += 5

while True:
    turtle.speed(random.randint(20,100))
    starspiral(random.randint(3, 30), random.randint(40,100))