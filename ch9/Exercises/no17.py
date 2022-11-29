

def remove_dups(astring):
    newStr = ''

    for i in astring:
        if i not in newStr:
            newStr += i
    
    return newStr


def main():
    a = remove_dups('mississippi')
    print(a)

if __name__ == '__main__':
    main()