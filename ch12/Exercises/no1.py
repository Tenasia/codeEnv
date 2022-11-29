def countLetter(string, letter):
    counter = 0
    for char in string:
        if char == letter:
            counter += 1
    return counter
def countOccurences(string):
    string = string.lower()
    countDict = {}
    for char in string:
        countDict[char] = countLetter(string, char)
    print('Letter\tOccurences')
    for key in sorted(countDict):
        occurences = countDict[key]
        print(f'{key}\t{occurences}')
def main():
    string = input('Please enter a string:')
    countOccurences(string)
if __name__ == '__main__':
    main()