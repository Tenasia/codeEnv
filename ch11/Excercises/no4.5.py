
import turtle
def plotRegression(t, wn):

    with open('D:\Downloads\codeEnv\ch11\Excercises\labdata.txt', 'r') as labdata:

        xList = []
        yList = []
        xyTuple = []

        sumOfX = 0
        sumOfY = 0

        xy = 0
        xx = 0
        n = 0


        for row in labdata:

            # Count the element on the list
            n += 1
            values = row.split()

            x = int(values[0])
            y = int(values[1])
            tuple = x, y

            xyTuple.append(tuple)
            xList.append(x)
            yList.append(y)

            sumOfX += x
            sumOfY += y

            # Multiply the x and y and find the sum
            xy += x * y
            xx += x * x
            

        meanOfX = sumOfX/n
        meanOfY = sumOfY/n

        numerator = xy - (n * meanOfX * meanOfY)
        denominator = xx - (n * (meanOfX * meanOfX))
        
        m = numerator/denominator

        yInterceptList = []
        for x in xList:
            yIntercept = meanOfY + m * (x - meanOfX)
            yInterceptList.append(yIntercept)


        wn.setworldcoordinates(-10, -10, max(xList[:])+10, max(yList[:])+10)
    
        t.up()
        for i in range(n):
            t.goto(xList[i], yList[i])
            t.dot()
            t.color("blue")
            t.goto(0, yIntercept)
            t.down()



        # print(a)
def main():

    wn = turtle.Screen()
    pr = turtle.Turtle()

    # wn.setworldcoordinates(-10, -10, 10, 10)
    pr.speed(1)

    plotRegression(pr, wn)

    wn.exitonclick()
    


if __name__ == '__main__':
    main()
