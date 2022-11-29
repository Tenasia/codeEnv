

from operator import indexOf


def removeSubstring(theString, subString):
    
    newString = ''
    index = len(subString)

    for i in range(len(theString)):
        if subString in theString[i:index + i]:
            newString += theString[index + i:]
            return newString
        else:
            newString += theString[i]


def main():
    
    a = removeSubstring('John Alvic P. Viojan', 'a')
    print(a)

if __name__ == '__main__':
    main()