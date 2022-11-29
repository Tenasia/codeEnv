


import random


def randomInteger(n):

    listofNums = []
    
    for i in range(n):
        a = random.randrange(n*10)
        listofNums.append(a)
    
    return listofNums

def mean(list):

    sum = 0
    for i in list:
        sum += i
    return sum / len(list)


def main():
    a = randomInteger(10)
    b = mean(a)
    print(b)

if __name__ == '__main__':
    main()