import string


def main():
    alphabetL = string.ascii_lowercase
    alphabetU = string.ascii_uppercase

    lyric = '''
    Road shimmer
    Wiggling the vision
    Heat heat waves
    I'm swimming in a mirror
    Road shimmer
    Wiggling the vision
    Heat heat waves
    I'm swimming in a
    Sometimes, all I think about is you
    Late nights in the middle of June
    Heat waves been faking me out
    Can't make you happier now
    Sometimes, all I think about is you
    Late nights in the middle of June
    Heat waves been faking me out
    Can't make you happier now
    '''

    a = alpCounter(lyric, alphabetU, alphabetL)
    print(a)

def alpCounter(lyrics, upperalph, loweralph):
    alphabetCount = 0
    letterECount = 0
    for letter in lyrics:
        if letter in upperalph or letter in loweralph:
            alphabetCount += 1
            if letter == 'e':
                letterECount += 1
        else:
            pass
    
    return f'Your text contains {alphabetCount} alphabetic characters, of which {letterECount} ({(alphabetCount / letterECount):.2f}%) are "e"'

        

if __name__ == '__main__':
    main()