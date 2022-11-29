
def sumTo(n):
    
    i = 0

    for number in range(n + 1):
        i += number

    return i


def main():
    
    print(sumTo(10))
    
    pass

if __name__ == '__main__':
    main()