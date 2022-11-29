
import random


def randomWords():

    words = ['hello', 'I', 'am', 'under', 'the', 'water']
    random.shuffle(words)
    
    newList = []
    for word in words:
       
        newList.append(word)
    
    return newList

def countWords(lst):
    count = 0
    for word in lst:
        if len(word) == 5:
            count += 1

    return count



def main():

    a = randomWords()
    print(a)
    b = countWords(a)
    print(b)

if __name__ == '__main__':
    main()