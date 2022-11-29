import turtle
import random

def drawDartBoard(t):

    t.penup()
    t.goto(0, -1)
    t.pendown()

    t.circle(1)

    t.penup()
    t.forward(1)
    t.left(90)
    t.pendown()

    for i in range(4):

        t.forward(2)
        t.left(90)

def throwDarts(t, darts = 100):

    
    t.penup()

    insideCount = 0

    for i in range(darts):
        randx = random.uniform(-1.0, 1.0)
        randy = random.uniform(-1.0, 1.0)

        x = randx
        y = randy

        t.goto(0, 0)

        distance_between = t.distance(x, y)
        print(distance_between)

        if distance_between < 1:
            t.color('red')
            insideCount += 1

        else:
            t.color('blue')

        t.goto(x, y)
        t.stamp()

    return insideCount


def main():

    wn = turtle.Screen()
    wn.setworldcoordinates(-1,-1,1,1)

    fred = turtle.Turtle()

    fred.speed(7)

    drawDartBoard(fred)
    darts = throwDarts(fred)

    print(darts)

    wn.exitonclick()

if __name__ == '__main__':
    main()
    



    

    
    


