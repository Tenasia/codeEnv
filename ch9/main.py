import ast
import turtle

def applyRules(ch):

    newstr = ''
    if ch == 'F':
        newstr = 'F-F++F-F'
    else:
        newstr = ch
    
    return newstr

def processString(oldString):
    newstr = ''

    for char in oldString:
        newstr += applyRules(char) 

    return newstr

def createLSystem(numiters, axiom):
    startString = axiom
    endString = ''
    for _ in range(numiters):
        endString = processString(startString)
        startString = endString  
    return endString
    
def drawLsystem(t, instruction, angle, distance):
    for command in instruction:
        if command == 'F':
            t.forward(distance)
        elif command == 'B':
            t.forward(-distance)
        elif command == '-':
            t.left(angle)
        elif command == '+':
            t.right(angle)
        
        else:
            pass

def count(text, char):
    lettercount = 0
    for c in text:
        if c == char:
            lettercount += 1
        else:
            pass
    return lettercount

def find(aString, aChar):
    '''Find and return the index of aChar in aString
       Return -1 if aChar is not found in aString
    '''

    index = 0
    found = False

    while not found and index < len(aString):
        if aString[index] == aChar:
            found = True
        else:
            index += 1
    
    if found:
        return index
    else:
        return -1   

def find2(aString, aChar, start = 0, end = None):

    ix = start

    if end == None:
        end = len(aString)

    found = False

    while not found and ix < end:
        if aString[ix] == aChar:
            found = True
        else:
            ix += 1
    
    if found:
        return ix
    else:
        return -1



def main():

    ss = "Python strings have some interesting methods."
    print(find2(ss, 's'))
    print(find2(ss, 's', 7))
    print(find2(ss, 's', 8))
    print(find2(ss, 's', 8, 13))
    print(find2(ss, '.'))


def commentSection():

    # startstring = 'A'
    # endstring = '<empty>'

    # for i in range(4):
    #   first iteration:
    #       endstring = 'B' 
    #       startstring = 'B'

    # startstring = 'B'
    # endstring = 'B'

    # for in range(4):
    #   second iteration:
    #       endstring = 'AB'
    #       startstring = 'AB'

    # startstring = 'AB'
    # endstring = 'BAB'

    # for i in range(4):
    #   third iteration:
    #       endstring = 'BAB'
    #       startstring = 'BAB'

    # starstring = 'BAB'
    # endstring = 'BAB'

    # for i in range(4):
    #   fourth iteration:
    #       endstring = 'ABBAB'
    #       starstring = 'ABBAB'

    # starstring = 'ABBAB'
    # endstring = 'ABBAB'

    # return endstring (endstring has now the value of ABBAB)
    pass


if __name__ == '__main__':
    main()