
import turtle


def applyRules(lhch):
    rule = ''

    if lhch == 'F':
        rule = 'F[-F]F[+F]F'
    else:
        rule = lhch

    return rule

def processStrings(oldString):
    newStr = ''
    for char in oldString:
        newStr += applyRules(char)
    
    return newStr

def createLSystem(IterNumber, axiom):
    startString = axiom
    endString = ''

    for _ in range(IterNumber):
        endString = processStrings(startString)
        startString = endString
    
    return endString

def drawLSystem(t, instruction, angle, distance):

    savedInfo = []
    for command in instruction:
        if command == 'F':
            t.forward(distance)
        elif command == 'B':
            t.forward(-distance)
        elif command == '+':
            t.right(angle)
        elif command == '-':
            t.left(angle)
        elif command == '[':
            savedInfo.append([t.heading(), t.xcor(), t.ycor()])
        elif command == ']':
            newInfo = savedInfo.pop()
            t.setheading(newInfo[0])
            t.goto(newInfo[1], newInfo[2])
        

def main():
    
    rules = createLSystem(4, 'F')

    wn = turtle.Screen()
    turtle1 = turtle.Turtle()
    turtle1.speed(0)
    turtle1.penup()
    turtle1.goto(0, -100)
    turtle1.pendown()
    turtle1.setheading(90)

    drawLSystem(turtle1, rules, 25, 5)

    wn.exitonclick()

if __name__ == '__main__':
    main()

