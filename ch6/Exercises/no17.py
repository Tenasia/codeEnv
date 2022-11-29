
import random
import turtle

def drawBar(t, height, width):

    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(width/2)

    t.fillcolor('black')
    writeHeight(t, height, width)

    t.forward(width/2)
    t.right(90)
    t.forward(height)
    t.left(90)

    if height >= 200:
        t.fillcolor('red')
    elif height >= 100:
        t.fillcolor('yellow')
    else:
        t.fillcolor('green')

def randomNumbers(list):

    numbers = []

    for _ in range(len(list)):
        rand_number = random.randint(min(list), max(list))
        numbers.append(rand_number)
    
    return numbers

def drawBars(t, heights, width):
  
    for height in heights:
        
        t.begin_fill()
        drawBar(t, height, width)
        t.end_fill()
    
    t.right(180)
    t.forward(width * len(heights))

def writeHeight(t, height, width):


    t.penup()
    t.left(90)
    t.forward(width/10)
    t.write(f'{height}', align='center')
    t.forward(-width/10)
    t.right(90)
    t.pendown()
        
def main():

    wn = turtle.Screen()

    data = [-48, -117, -200, -240, -160, -260, -220]
    
    list = randomNumbers(data)
    max_list = max(list)
    min_list = min(list)
    border = 10

    wn.setworldcoordinates(0 - border, 0 - border, 40*len(list) + border, max_list + border)

    bar = turtle.Turtle()

    bar.speed(5)

    bar.penup()
    bar.goto(0, 0)
    bar.pendown()

    drawBars(bar, list, 40)

    wn.exitonclick()

if __name__ == '__main__':
    main()