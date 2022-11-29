# Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and including n. 
# So sumTo(10) would be 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2.

def sumTo(n):
    sum = 0
    for i in range(n + 1):
        sum += i

    return sum

def sumTo1(n):

    sum = n * (n+1) / 2
    return sum

def main():

    print(sumTo(10))
    # or 
    print(sumTo1(10))
    


if __name__ == '__main__':
    main()