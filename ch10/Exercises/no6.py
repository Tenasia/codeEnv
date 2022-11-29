''' Write a function to count how many odd numbers are in a list. '''
import random

def randomInteger(n):

    listofNums = []
    
    for i in range(n):
        a = random.randrange(n*10)
        listofNums.append(a)
    
    return listofNums


def countOdd(lst):
    
    count = 0

    for i in lst:
        if i % 2 == 0:
            pass
        else:
            count += 1

    return count

def main():
    a = randomInteger(10)
    print(a)
    b = countOdd(a)
    print(b)

if __name__ == '__main__':
    main()