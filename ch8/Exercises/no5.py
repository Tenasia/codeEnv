
import random
import turtle


def isInScreen(t, wn):

    upperBound = wn.window_height() / 2
    lowerBound = - wn.window_height() / 2
    leftBound = - wn.window_width() / 2
    rightBound = wn.window_width() / 2

    xpos = t.xcor()
    ypos = t.ycor()

    if xpos > rightBound or xpos < leftBound:
        return False
    elif ypos > upperBound or ypos < lowerBound:
        return False
    else:
        return True

def moveRandom(t, sz):

    coinFlip = random.randrange(0, 2)

    if coinFlip == 0:
        t.left(random.randrange(90))
    else:
        t.right(random.randrange(90))

    t.forward(sz)

def closeTogether(t, t2):
    
    if t.distance(t2) < 2:
        return False
    else:
        return True

def main():
    
    wn = turtle.Screen()

    turts = turtle.Turtle()
    turts.speed(7)
    turts1 = turtle.Turtle()
    turts1.speed(7)

    turts.penup()
    turts.goto(- wn.window_width() / 3, 0)
    turts.pendown()
    turts1.penup()
    turts1.goto(wn.window_width() / 3, 0)
    turts1.pendown()


    while isInScreen(turts, wn) and isInScreen(turts1, wn) and closeTogether(turts, turts1):
        moveRandom(turts, 50)
        moveRandom(turts1, 50)

    wn.exitonclick()



if __name__ == '__main__':
    main()