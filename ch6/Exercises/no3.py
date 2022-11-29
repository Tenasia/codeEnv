#3. Draw a polygon that has a input argument of the sides, and the size (of course the turtle is always there.))
import turtle

def drawPoly(t, sides, size):

    angle = 360/sides

    for _ in range(sides):
        t.forward(size)
        t.left(angle)

def main():
    wn = turtle.Screen()
    poly1 = turtle.Turtle()


    drawPoly(poly1, 8, 50)

    wn.exitonclick()

if __name__ == '__main__':
    main()