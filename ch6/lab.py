# What should we use as the number of sides?
# == 360
# What should we use as the side length
# 2 * pi * radius (360)

import turtle

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.left(turnAngle)

def drawCircle(anyTurtle, radius):
    
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)


wn = turtle.Screen()
wheel = turtle.Turtle()

wheel.speed(1)

def drawCircleCenter(t, r):

    t.penup()
    t.forward(r)
    t.left(90)
    t.pendown()

    drawCircle(t, r)

    t.penup()
    t.left(90)
    t.forward(r)
    t.pendown()

r = 100

# drawCircle(wheel, r)
drawCircleCenter(wheel, r)



wn.exitonclick()

# Draw a circle around the center point of the turtle

# Let's break it down: Draw a square first, and then make sure so that the square is drawn centered around the turtle's starting point.