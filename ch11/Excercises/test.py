import turtle   
def drawTurtle(myFile, myTurtle):
    line = f.readline()
    while line:
        dataline = line.split()
        
        if dataline[0] == "UP":
            myTurtle.penup()
            
        elif dataline[0] == "DOWN":
            myTurtle.pendown()
            
        else:
            x,y = int(dataline[0]), int(dataline[1])
           
            myTurtle.goto(x,y)
        
        line = f.readline()
            
#file opening       
f = open('D:\Downloads\codeEnv\ch11\Excercises\mystery.txt', "r")

#turtle creating
ryan = turtle.Turtle()

#Screen setting
screen = turtle.Screen()
screen.setworldcoordinates(-300, -300, 300, 300)       
drawTurtle(f, ryan)

f.close()
wn.exitonclick()