import turtle
from turtle import TurtleGraphicsError
import math
from random import randrange
def drawSquare(t, size):

    for i in range(4):
        t.forward(size)
        t.left(90)

def drawMultiSquares(t):

    size = 20
    for i in range(5):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90)
        t.forward(size)
        
        t.penup()
        t.forward(10)
        t.left(90)
        t.forward(-10)
        t.pendown()

        size += 20

def drawPoly(t, sides, size):
    
    angle = 360/sides
    for i in range(sides):
        t.forward(size)
        t.left(angle)

def prettyPattern(t, size):

    for i in range(24):
        t.left(90/6)
        drawSquare(t, size)

def twoSpirals(t):

    size = 5
    for i in range(100):
        t.right(90)
        t.forward(size)
        size += 5
    
    t.penup()
    t.goto(0, 0)
    t.pendown()

    size = 5
    for i in range(100):
        t.right(91)
        t.forward(size)

        size += 5
        
def drawEquitriangle(t, size):

    drawPoly(t, 3, size)    

def sumTo(n):

    sum1 = 0
    for i in range(n + 1):
        sum1 += i

    sum2 = n * (n + 1) / 2
    return sum1, sum2

def areaOfCircle(r):
    
    area = math.pi * math.pow(r, 2)
    return int(area)

def drawStar(t, size):

    for i in range(5):
        t.forward(size)
        t.right(720/5)

def drawStars(t, size):

    for i in range(5):
        t.penup()
        t.forward(350)
        t.right(720/5)
        t.pendown()
        drawStar(t, size)

def drawStarN(t, sides, size):

    if sides < 3 or sides % 2 == 0:
        return "Not a valid number of sides for a star."

    for i in range(sides):
        t.forward(size)
        t.left(720/sides)

def drawSprite(t, legs, size):
    for i in range(legs):
        t.forward(size)
        t.forward(-size)
        t.left(360/legs)
        
def sumTo1(n):
    
    sum = 0
    for i in range(n + 1):
        sum += i
    print(sum)
    return sum

def mySqrt(n):
    guess = n/2
    for i in range(n):
        print(guess)
        guess = (1/2) * (guess + (n/guess))
    print(int(guess))

def myPi(n):

    sign = 1
    pi = 0

    denominator = 1

    for i in range(n):
        pi += (sign/denominator)
        sign *= -1
        denominator += 2
    
    pi *= 4
    print(pi)

def fancySquare(t, shape):
    
    shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
        
    if shape not in shapes:
        return 'not a valid shape'

    t.shape(shape)
    
         
    for _ in range(4):
        t.forward(100)
        t.stamp()
        t.left(90)
    
def drawBars(t, n_list, wn):

    wn.setworldcoordinates(0, 0, 500, 500)

    for size in n_list:
        t.left(90)
        t.forward(size)
        t.right(90)
        t.forward(25)
        t.left(90)
        t.penup()
        t.forward(12.5)
        t.write(size, align='center')
        t.forward(-12.5)
        t.right(90)
        t.pendown()
        t.forward(25)
        t.right(90)
        t.forward(size)
        t.left(90)
    
    t.left(180)
    t.forward(len(n_list) * 50)

def randomInt():

    random_integers = []
    for i in range(5):
        randomizer = randrange(0, 250)
        random_integers.append(randomizer)
    return random_integers
def main():

    wn = turtle.Screen()
    t = turtle.Turtle()
    
    t.speed(5)
    
    r_int = randomInt()
    drawBars(t, r_int, wn)

    wn.exitonclick()

if __name__ == '__main__':
    main()