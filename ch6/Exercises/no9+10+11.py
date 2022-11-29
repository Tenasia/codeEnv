import turtle

def drawStar(t, sz, n = 5):

    for _ in range(n):
        t.forward(sz)
        t.right(720/n)

def drawStars(t, sz, n = 5):

    for _ in range(n):

        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()
        drawStar(t, sz, n)

def drawStarN(t, sz, n):

    if (n % 2) == 0:
        print('Not a valid star points e.g it must be odd number')
        return
    elif n < 3:
        print('Not enough lines to draw a star-esque shape')
        return
    else:
        pass

    drawStar(t, sz, n)

def main():

    wn = turtle.Screen()
    star = turtle.Turtle()
    
    drawStarN(star, 100, 9)

    wn.exitonclick() 

if __name__ == '__main__':

    main()