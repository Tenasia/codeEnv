

import turtle

colors = {0:"red", 1:"purple", 2:"hotpink", 3:"lightblue"}


def makeSquare(turtle, size):
    """ Makes a square """
    for color in colors.keys():
        turtle.color(colors[color])
        turtle.forward(size)
        turtle.left(90)
    
    
wn = turtle.Screen()

sq1 = turtle.Turtle()



def makeMultipleSquares():
    size = 50
    for i in range(15):
        makeSquare(sq1, size)
        size += 25
        sq1.forward(10)
        sq1.right(18)

makeMultipleSquares()

wn.exitonclick()

