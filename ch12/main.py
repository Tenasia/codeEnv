def countAll(string):

    empty_dic = {}
    for chr in string:
        empty_dic[chr] = string.count(chr)
        # empty_dic[chr] = countA(string, chr)

    print(empty_dic)

def countA(string, letter):
    count = 0
    for chr in string:
        if chr == letter:
            count += 1
    return count

def main():
    countAll('banana')

if __name__ == '__main__':
    main()

    