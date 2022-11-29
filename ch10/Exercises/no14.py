
import turtle


def applyRule(lhch):

    rule = ''

    if lhch == 'H':
        rule = 'HFX[+H][-H]'
    elif lhch == 'X':
        rule = 'X[-FFF][+FFF]FX'
    else:
        rule = lhch
    
    return rule

def processStrings(oldString):
    newStr = ''

    for char in oldString:
        newStr += applyRule(char)
    
    return newStr
def createLSystem(iterNumber, axiom):
    startString = axiom
    endString = ''

    for _ in range(iterNumber):
        endString = processStrings(startString)
        startString = endString
    
    return endString

def drawLSystem(t, instruction, angle, distance):

    savedInfoList = []
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
            savedInfoList.append([t.heading(), t.xcor(), t.ycor()])
        elif command == ']':
            newInfo = savedInfoList.pop()
            t.setheading(newInfo[0])
            t.goto(newInfo[1], newInfo[2])
        else:
            pass

def main():

    wn = turtle.Screen()

    turtle1 = turtle.Turtle()
    turtle1.speed(0)

    rules = createLSystem(4, 'H')
    print(rules)
    drawLSystem(turtle1, rules, 27.5, 5)
    wn.exitonclick()
if __name__ == '__main__':
    main()