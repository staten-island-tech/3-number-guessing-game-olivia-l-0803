print("Yay!!! You completed the game!! You will get FREE private tickets to the turtle show! :-P")

import turtle
turtle.shape("turtle")

def star(length):
    for i in range(5):
        turtle.forward(length)
        turtle.right(144)

star(50)