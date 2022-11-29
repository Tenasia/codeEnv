# 5. Draw two spiral, one that is square-like but increases in length, one is angled by 1 degrees less 

import turtle


def lineSpiral(t, angle):

    move = 5

    for _ in range(50):
        t.right(angle)
        t.forward(move)

        move += 5
    
def angledSpiral(t):

    lineSpiral(t, 89)

def combinedSpiral(t):

    t.penup()
    t.goto(-200, 0)
    t.pendown()

    lineSpiral(t, 90)

    t.penup()
    t.goto(150, 0)
    t.pendown()

    angledSpiral(t)

def main():
    wn = turtle.Screen()
    sprl = turtle.Turtle()
    sprl.speed(7)
    
    combinedSpiral(sprl)


    wn.exitonclick()

if __name__ == '__main__':
    main()