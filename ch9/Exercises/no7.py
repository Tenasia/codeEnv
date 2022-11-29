



def remove_letter(theLetter, theString):

    newString = ''
    for char in theString:
        if char != theLetter:
            newString += char
        else:
            pass
    return newString

def main():
    a = remove_letter('a', 'hehehahahashgaheas')
    print(a)

if __name__ == '__main__':
    main()
