
import random

def randomInteger(n):

    listofNums = []
    
    for i in range(n):
        a = random.randrange(n*10)
        listofNums.append(a)
    
    return listofNums

def sumUntilEven(lst):
    sum = 0
    for i in lst:
        if i % 2 != 0:
            sum += i
        else:
            return sum
    return sum

a = randomInteger(10)
b = sumUntilEven(a)
print(a)
print(b)