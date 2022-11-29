'''Count how many words occur in a list up to and including the first occurrence of the word “sam”.'''


def count(lst):
    words = ['test', 'tert', 'help', 'sam', 'I dont', 'understand' ,'it'  ,'sam']
    print(words)
    count = 0
    for word in words:
        
        if word == 'sam':
            return count
        else:
            count += 1
    return count


def main():
    
    a = count('test')
    print(a)


if __name__ == '__main__':
    main()