from tracemalloc import start
import turtle


def applyRules(character):

    rule = ''
    if character == 'F':
        rule = 'FF'
    elif character == 'X':
        rule = '--FXF++FXF++FXF--'
    else:
        rule = character
    
    return rule

def processStrings(oldString):
    newString = ''

    for char in oldString:
        newString += applyRules(char)
    
    return newString

def createLSystem(iterNumber, axiom):
    startString = axiom
    endString = ''

    for _ in range(iterNumber):
        endString = processStrings(startString)
        startString = endString

    return endString

def drawSierpinskiTriangle(t, instructions, angle, distance):
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
    a = createLSystem(4, 'FXF--FF--FF')
    print(a)

    wn = turtle.Screen()
    Sierpinski = turtle.Turtle()
    Sierpinski.speed(0)

    drawSierpinskiTriangle(Sierpinski, a, 60, 5)

    wn.exitonclick()

if __name__ == '__main__':
    main()