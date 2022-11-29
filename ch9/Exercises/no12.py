


import turtle


def applyRule(lhch):
    newstr = ''

    if lhch == 'L':
        newstr = '+RF-LFL-FR+'
    elif lhch == 'R':
        newstr = '-LF+RFR+FL-'
    else:
        newstr = lhch

    return newstr
def processString(oldString):
    newStr = ''

    for char in oldString:
        newStr += applyRule(char)

    return newStr

def createLSystem(iterNumber, axiom):
    startString = axiom
    endString = ''

    for _ in range(iterNumber):
        endString = processString(startString)
        startString = endString

    return endString

def draw(t, instructions, angle, distance):

     for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == 'B':
            t.backward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)
    
def main():
    wn = turtle.Screen()
    turtleL = turtle.Turtle()

    turtleL.speed(0)

    instructions = createLSystem(4, 'L')

    draw(turtleL, instructions, 90, 5)
    wn.exitonclick()

if __name__ == '__main__':
    main()