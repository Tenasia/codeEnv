import random

def randomInteger(n):

    listofNums = []
    
    for i in range(n):
        a = random.randrange(n*10)
        listofNums.append(a)
    
    return listofNums


def sumEven(lst):
    
    sum = 0

    for i in lst:
        if i % 2 == 0:
            sum += i

    return sum

def main():
    a = randomInteger(10)
    print(a)
    b = sumEven(a)
    print(b)

if __name__ == '__main__':
    main()