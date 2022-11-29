# 1.) Draw Square 4 times, equal spacing

import turtle

def drawSquare(t, length):

    t.penup()
    t.forward(length * 2)
    t.pendown()
    
    for _ in range(4):
        t.forward(length)
        t.left(90)
    
def drawSquares(t, length):


    for _ in range(5):

        drawSquare(t, length)

    t.penup()
    t.forward(length * 2)
    t.pendown()

def main():

    wn = turtle.Screen()
    wn.setworldcoordinates(0, -125, 250, 125)

    squareT = turtle.Turtle()

    drawSquares(squareT, 20)

    wn.exitonclick()


if __name__ == '__main__':
    main()