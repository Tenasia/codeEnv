
import random


def randomInteger(n):

    listofNums = []
    
    for i in range(n):
        a = random.randrange(n*10)
        listofNums.append(a)
    
    return listofNums


def max(list):

    if list == []:
        return 'not a valid list.'

    max = list[0]

    for i in list:
        if max < i:
            max = i
    
    return max


def main():
    a = randomInteger(10)
    print(a)
    b = max(a)

    print(b)

if __name__ == '__main__':
    main()