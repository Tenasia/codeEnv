import turtle

def main():
 

    wn = turtle.Screen()
    

    dt = turtle.Turtle()
    
    plotBar(dt, 'HelloHellomadafekers', wn)

    wn.exitonclick()

def plotBar(t, string, window):   


    window.setworldcoordinates(0, 0, len(string) + 1, len(string) + 1)

    string = string.lower()
    dictList = {}
    for char in string:
        dictList[char] = countCharacters(string, char)

    
    for letter in sorted(dictList):

        count = dictList[letter]

        t.left(90)
        t.forward(count)
        t.right(90)
        t.forward(0.5)
        t.write(letter)
        t.penup()
        t.left(90)
        t.forward(0.25)
        t.write(count)
        t.forward(-0.25)
        t.right(90)
        t.pendown()
        t.forward(0.5)
        t.right(90)
        t.forward(count)
        t.left(90)

def countCharacters(string, letter):

    count = 0

    for char in string:
        if char == letter:
            count += 1
    
    return count

if __name__ == '__main__':
    main()