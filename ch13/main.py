
import turtle
import time

def drawPoly(t, size, window):
    try:
        n = int(input('Draw a shape with how many points! '))
        angle = 360/n
        for i in range(n):
            t.forward(size)
            t.right(angle)
        time.sleep(3)
    except Exception as e:
        print("Not enough sides")
        print(e)
    finally:
        window.bye()



def main():
    wn = turtle.Screen()
    tess = turtle.Turtle()
    drawPoly(tess, 100, wn)


if __name__ == '__main__':
    main()