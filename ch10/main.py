
from copyreg import add_extension
import turtle
from venv import create


def applyRules(character):

    rule = ''
    if character == 'X':
        rule = 'F[-X]+X'
    elif character == 'F':
        rule = 'FF'
    else:
        rule = character
    
    return rule

def processString(oldString):
    newString = ''

    for char in oldString:
        newString += applyRules(char)
    
    return newString

def createLSystem(iterNumber, axiom):
    startString = axiom
    endString = ''

    for _ in range(iterNumber):
        endString = processString(startString)
        startString = endString
    
    return endString

def drawTree(t, instruction, angle, distance):

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
    instruction = createLSystem(6, 'X')
    
    wn = turtle.Screen()
    tree = turtle.Turtle()
    tree.speed(0)
    tree.left(90)
    drawTree(tree, instruction, 30, 2)

    wn.exitonclick()

if __name__ == '__main__':
    main()