import random


def randomInteger(n):

    listofNums = []
    
    for i in range(n):
        a = random.randrange(n*10)
        listofNums.append(a)
    
    return listofNums

def sum_of_squares(xs):

    sum = 0

    for i in xs:
        squared = i * i
        sum += squared
    
    return sum



def main():
    a = randomInteger(3)
    print(a)
    b = sum_of_squares(a)

    print(b)

if __name__ == '__main__':
    main()