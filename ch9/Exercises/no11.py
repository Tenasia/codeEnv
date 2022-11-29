
def commentSection():
    
    # counter = 0
    # word = 'banana'

    # while 'na' in 'banana':
    #   counter += 1
    #   leftIndex = 2
    #   rightIndex = 2 + 2
    #   word = word[4: ] + word[ :2]

    # counter = 1
    # word = 'naba'

    # while 'na' in 'banana':
    #   counter += 1
    #   leftIndex = 0
    #   rightIndex = 2 + 0
    #   word = word[2: ] + word[ :0]

    # counter = 2
    # word = 'ba'

    # while 'na' in 'banana':
    #   counter += 1
    #   leftIndex = -1
    #   rightIndex = 2 + -1
    #   word = word[1: ] + word[:-1]

    # ^ while the code inside the body execute, it won't return anything as the while loop is now false. like you can put a print inside of it and you will see that the counter is 3 while it is 2 in return output of the function.
    pass

def countfor(subStr, theStr):

    counter = 0
    word = theStr
    index = len(subStr)
    for i in range(len(theStr)):
        if subStr in word[i: index + i]:
            counter += 1
    
    return counter

def countwhile(subStr, theStr):

    counter = 0 
    word = theStr
    while subStr in word:
        counter += 1
        leftIndex = word.find(subStr)
        rightIndex = len(subStr) + leftIndex
        word = word[rightIndex:] + word[:leftIndex]

    return counter

def removefor(subStr, theStr):
    
    newStr = ''
    index = len(subStr)
    word = theStr
    for i in range(len(word)):
        if subStr in word[i:index + i]:
            newStr += word[index + i:]
        else:
            newStr += word[i]
    return -1
def remove(substr, theStr):

    newString = ''
    word = theStr
    while substr in word:
        newString += theStr.replace(substr, '' ,1)
        print(newString)
        word = newString
        print(word)
        if word == 'bana':
            break
        else:
            print('it passed')
    return newString

def removeWhile(subStr, theStr):

    word = theStr
  
    while subStr in word:
        leftIndex = word.find(subStr)
        rightIndex = len(subStr) + leftIndex
        word = word[:leftIndex] + word[rightIndex:]
    
    return word

# word = 'banana'

# while 'na' in 'banana':
#       leftIndex = 2
#       rightIndex = 2 + 2
#       word = word[0:2] + word[4:]
#       word = 'ba' + 'na'

# word = 'bana'

# while 'na' in 'bana':
#   leftIndex = 2
#   rightindex = 2 + 2
#   word = word[0:2] + word[4:]
#   word = 'ba' + ''

# word = 'ba'


# while 'na' in 'ba' = False

# return word



def main():

    a = countfor('na', 'banana')
    b = countwhile('na', 'banana')
    c = removefor('na', 'banana')
    d = removeWhile('na', 'banana')

    # strObj = 'this is a sample String'
    # subStr = 'is'
    # index = strObj.find(subStr)
    # start = 5
    # stop = 10

    # if len(strObj) > stop:
    #     strObj = strObj[0:index] + strObj[index + len(subStr):]


    print(d)


    



if __name__ == '__main__':

    main()  