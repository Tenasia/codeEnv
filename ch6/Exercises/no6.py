# Write a non-fruitful function drawEquitriangle(someturtle, somesize) 
# which calls drawPoly from the previous question to have its turtle draw a equilateral triangle.


import no3

# Imported a previous module so I can still use the imports from there and lesser calling

def equalTriangle(t, sz):

    no3.drawPoly(t, 3, sz)


def main():

    wn = no3.turtle.Screen()

    triangle = no3.turtle.Turtle()

    equalTriangle(triangle, 100)


    wn.exitonclick()

if __name__ == '__main__':
    main()