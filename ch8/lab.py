


import turtle


def n3(n):

    steps = 0
    while n != 1:
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

        steps += 1

    return steps


def drawIter(t):

    maxSoFar = 0

    for i in range(1, 50 + 1):

        steps = n3(i)

        t.left(90)
        t.forward(steps)
        t.right(90)
        t.forward(0.5)
        t.write(i, align='center')

        if steps >= 100:   
            t.penup()
            t.left(90)
            t.forward(5)
            t.write(str(steps), align='center')
            t.forward(-5)
            t.right(90)
            t.pendown()

        t.forward(0.5)
        t.right(90)
        t.forward(steps)
        t.left(90)
        
        
        if maxSoFar < steps:
            maxSoFar = steps
            print(maxSoFar)

def main():

    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, 51, 150)

    graph = turtle.Turtle()
    graph.speed(0)
    graph.goto(0, 0)
    
    drawIter(graph)


    wn.exitonclick()


if __name__ == '__main__':
    main()