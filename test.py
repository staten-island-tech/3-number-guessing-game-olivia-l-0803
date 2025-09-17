print("Yay!!! You completed the game!! You will get FREE private tickets to the turtle show! :-P")

import turtle
import random
turtle.shape("turtle")

def star(length):
    for i in range(5):
        turtle.forward(length)
        turtle.right(144)

star(50)

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
    turtle.clear()