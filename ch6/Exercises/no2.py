# 2. Draw squares with increasing size of 20, hint the gap between each side is 10

import turtle


def drawSquare(t, sz):

    for _ in range(4):
        t.forward(sz)
        t.left(90)

def main():

    wn = turtle.Screen()
    sq1 = turtle.Turtle()

    wn.setworldcoordinates(-150, -150, 150, 150)

    drawSquares(sq1, 20)

    wn.exitonclick()


def drawSquares(t, sz):
    upsize = 0
    for _ in range(5):
        drawSquare(t, sz + upsize)
        t.penup()
        t.forward(30 + upsize)
        t.left(90)
        t.forward(30 + upsize)
        t.left(90)
        t.pendown()

        upsize += 20

if __name__ == '__main__':
    main()