
import no12

def drawFancySquare(t, size, n):

    for _ in range(4):
        t.forward(size * 2)
        no12.drawSprite(t, size, n)
        t.left(90)


    

def main():
    wn = no12.turtle.Screen()
    fancy = no12.turtle.Turtle()



    drawFancySquare(fancy, 50, 12)
    wn.exitonclick()



if __name__ == '__main__':

    main()