
import turtle


def applyRules(character):

    rule = ''

    if character == 'X':
        rule = 'X+YF+'
    elif character == 'Y':
        rule = '-FX-Y'
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
    for i in range(iterNumber):
        endString = processString(startString)
        startString = endString
    
    return endString

def drawDragon(t, instructions, angle, distance):
    for command in instructions:
        if command == 'F':
            t.forward(distance)
        elif command == 'B':
            t.forward(-distance)
        elif command == '+':
            t.right(angle)
        elif command == '-':
            t.left(angle)
        else:
            pass
    
def main():

    wn = turtle.Screen()
    dragon = turtle.Turtle()
    commander = createLSystem(10,'FX')

    drawDragon(dragon, commander, 60, 5)
    wn.exitonclick()
if __name__ == '__main__':
    main()