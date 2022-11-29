#4. Draw a pretty pattern, hint 5 squares that rotates



import turtle

def drawSquare(t, size):

    for _ in range(4):
        t.forward(size)
        t.left(90)

def prettyPattern(t, size):

    squares = 20
    for _ in range(squares):
        drawSquare(t, size)
        # I found this angle by first drawing a square that has line each direction e.g (north, east, south, west), and thought that there's a 5 lines in all of the quadrants, divide that by the circle size which is 360 and you get 18
        t.left(360/squares)



def main():
    wn = turtle.Screen()
    prt = turtle.Turtle()

    prettyPattern(prt, 50)
    
        


    

    wn.exitonclick()

if __name__ == '__main__':
    main()