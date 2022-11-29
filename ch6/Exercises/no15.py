
def myPi(n):
    
    '''returns approximation of pi using leibniz formula for pi'''

    denominator = 1
    sum = 0

    for _ in range(n):
        sum = sum + 1/denominator - 1/(denominator + 2)
        denominator += 4
    
    pi = sum * 4

    return pi

def myPi1(n):

    denominator = 1
    sum = 0
    for _ in range(n):
        sum = sum + 4/denominator - 4/(denominator + 2)
        denominator += 4
    
    return sum


def main():

    print(myPi1(100000))
    

if __name__=='__main__':
    main()