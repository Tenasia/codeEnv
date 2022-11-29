import random

def randomInteger(n):

    listofNums = []
    
    for i in range(n):
        a = random.randrange(-100, 100)
        listofNums.append(a)
    
    return listofNums


def sumNegatives(lst):
    
    sum = 0
    for i in lst:
        if i < 0:
            sum += i

    return sum

def main():
    a = randomInteger(10)
    print(a)
    b = sumNegatives(a)
    print(b)

if __name__ == '__main__':
    main()