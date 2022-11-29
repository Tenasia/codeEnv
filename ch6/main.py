import random
import turtle


def drawBar(t, height, color):

    t.begin_fill()
    t.fillcolor(str(color))
    t.left(90)
    t.forward(height)
    t.right(90)
    t.write(str(height))
    t.forward(50)
    t.right(90)
    t.forward(height)
    t.left(90)

    t.end_fill()

def drawBars(turtle, heights, color):
    
    for height in heights:
        drawBar(turtle, height, color)
    
    turtle.goto(0, 0)
    
def main():

    
    heights_of_bars = [48, 117, 200, 240, 160, 260, 220]

    max_height = max(heights_of_bars)
    number_of_bars = len(heights_of_bars)
    border = 10

    wn = turtle.Screen()
    wn.setworldcoordinates(0 - border, 0 - border, 50*number_of_bars + border, max_height + border)

    t = turtle.Turtle()
    
    t.goto(0, 0)

    drawBars(t, heights_of_bars, 'lightgreen')
    # if you want random heights but still uses the values from the height_of_bars:

    random_height = []
    
    for i in range(7):
        rint = random.randint(min(heights_of_bars), max(heights_of_bars))
        random_height.append(rint)
    
    drawBars(t, random_height, 'lightblue')


    wn.exitonclick()

if __name__ == '__main__':
    main()
