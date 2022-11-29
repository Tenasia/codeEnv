

from statistics import mean
import turtle
def plot_regression(t):

    with open('D:\Downloads\codeEnv\ch11\Excercises\labdata.txt', 'r') as ld:
        
        
        listOfX = []
        listOfY = []
        
        listOfTuples = []
        sumX = 0
        sumY = 0
        n = 0
        for row in ld:
            coordinates = row.split(' ')
            
            x = int(coordinates[0])
            y = int(coordinates[1])

            tuple = x, y
            listOfX.append(x)
            listOfY.append(y)

            sumX += x
            sumY += y
        
            listOfTuples.append(tuple)
            n += 1
        
        listOfM = []

        for i in listOfTuples:
            x, y = i
            numerator = (sumX * sumY) - (n * x * y)
            denominator = (sumX ** 2) - (n * x**2)
            m = numerator / denominator
            listOfM.append(m)

        meanOfX = mean(listOfX)
        meanOfY = mean(listOfY)
    
        listOfYandM = []

        for m in listOfM:
            y = meanOfY + m * (x - meanOfX)
            listOfYandM.append(y)
        
        t.up()
        for i in range(n):
            t.goto(listOfX[i], listOfY[i])
            t.dot()
            t.color('blue')
            t.goto(0, listOfYandM[i])
            t.down()
            t.goto(max(listOfX[:]), listOfYandM[i] + listOfM[i])




def main():
    
    
    
    
    wn = turtle.Screen()
    turtle1 = turtle.Turtle()
    plot_regression(turtle1)
    wn.exitonclick()

if __name__ == '__main__':
    main()