import turtle


def drawSprite(t, sz, n):

    for _ in range(n):
        t.forward(sz)
        t.stamp()
        t.forward(-sz)
        t.right(360/n)


def main():
    wn = turtle.Screen()
    sprite = turtle.Turtle()


    drawSprite(sprite, 120, 15)

    wn.exitonclick()
    pass

if __name__ == '__main__':
    main()