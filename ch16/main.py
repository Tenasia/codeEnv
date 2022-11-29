
import turtle

# Example of Recursive functions

def sumList(list):

    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sumList(list[1:])

def fact(n):
    

    if n <= 1:
        return n
    else:
        return n * fact(n - 1)

def reverse(s):

    if len(s) == 1:
        return s[0]
    else:
        return reverse(s[1:]) + s[0]

def isPal(string):

    if string == reverse(string):
        return True
    else:
        return False

def removeWhiteSpace(string):

    if len(string) == 1:
        return string[0]
    elif len(string) == 0:
        return ' '
    elif string[0] == ' ':
        return string[1] + removeWhiteSpace(string[2:])
    
    else:
        return string[0] + removeWhiteSpace(string[1:])

def drawFractalTree(branchLen, t):
    
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        drawFractalTree(branchLen-15,t)
        t.left(40)
        drawFractalTree(branchLen-15, t)
        t.right(20)
        t.backward(branchLen)
        # t.left(40)
        # drawFractalTree(branchLen-10,t)
        # t.right(20)
        # t.backward(branchLen)
    
# if 75 > 5:
#   t.forward(75)
#   t.right(20)
#   drawFractalTree(75 - 15, t):
#       if 60 > 5:
#           t.forward(75)
#           t.right(20)
#           drawFractalTree(60 - 15, t):
#               if 45 > 5:
#                   t.forward(45)
#                   t.right(20)
#                   drawFractalTree(45 - 15, t):
#                      if 45 > 5:
    #                      t.forward(30)
    #                      t.right(20)
#                      drawFractalTree(30 - 15, t):
#                           t.forward(15)
#                           t.right(20)
#                           drawFractalTree(15 - 15, t):
#                           t.left(40)
#                           drawFractalTree(15 - 15, t):
#                           t.right(20)
#                           t.backward(15)
#                      t.left(40)
#                      drawFractalTree(30 - 15, t):
#                      t.right(20)
#                      t.backward(30)
#                   t.left(40)
#                   drawFractalTree(45 - 15, t):
#                   t.right(20)
#                   t.backward(45)
#           t.left(40)
#           drawFractalTree(60 - 15, t):
#           t.right(20)
#           t.backward(60)
#   t.left(40)
#   drawFractalTree(75 - 15, t):
#   t.right(20)
#   t.backward(75)
 
def main():
    
    wn = turtle.Screen()
    t = turtle.Turtle()

    
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')

    drawFractalTree(75, t)

    wn.exitonclick()
    


if __name__ == '__main__':
    main()

print(isPal(removeWhiteSpace('')))

