
import random

def randomInteger(n):

    listofNums = []
    
    for i in range(n):
        a = random.randrange(n)
        listofNums.append(a)
    
    return listofNums

def count(list, item):
    count = 0

    for i in list:
        if i == item:
            count += 1
    
    return count

def isIn(list, item):

    if item in list:
        return True
    else:
        return False

def reverse(list):

    reversedList = []

    for i in list:
        reversedList = [i] + reversedList

    return reversedList

def indexOf(list, item):

    index = 0

    for i in list:
        if i == item:
            return index
        else:
            index += 1

    return index
def insert(list, index, item):

    inserted_list = list[:index] + [item] + list[index:]
    return inserted_list
def main():
    
    a = randomInteger(10)
    print(a)
    b = count(a, 2)
    print(b)
    c = isIn(a, 8)
    print(c)
    d = reverse(a)
    print(d)
    e = indexOf(a, 8)
    print(e)

    f = insert(a, 6, 15)
    print(f)
if __name__ == '__main__':
    main()