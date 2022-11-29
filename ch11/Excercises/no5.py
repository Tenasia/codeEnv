
import turtle
def drawFile(t):

    with open('D:\Downloads\codeEnv\ch11\Excercises\mystery.txt') as plotPoints:

        for row in plotPoints:
            values = row.split()

            if values[0] == 'UP':
                t.penup()
            elif values[0] == 'DOWN':
                t.pendown()
            else:
                x = int(values[0])
                y = int(values[1])

                t.goto(x, y)

               

def main():

    wn = turtle.Screen()
    filedraw = turtle.Turtle()

    drawFile(filedraw)
    wn.exitonclick()

if __name__ == '__main__':
    main()