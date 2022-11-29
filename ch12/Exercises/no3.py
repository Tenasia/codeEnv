


def main():
    everyWord()

def everyWord():
    with open('D:\Downloads\codeEnv\ch12\Exercises\\alice_words.txt', 'r') as file:
    
        print('Word\t\tCount')

        table = ''
        every_word = []
        
        for row in file:
            letter_word = row.split()

            for each_word in letter_word:
                each_word = each_word.lower()
                every_word.append(each_word)

        countDict = {}
        
        for word in every_word:
            countDict[word] = countString(every_word, word)
        
        max = 0
        for key in sorted(countDict):
            counter = countDict[key]

            if max < counter:
                max = counter

            table += f'{key}\t\t{counter}\n'
        
        print(countDict)
        
    

def countString(list, word):
    count = 0
    for char in list:
        if char == word:
            count += 1
    return count

if __name__ == '__main__':
    main()