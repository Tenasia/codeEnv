


def mySqrt(n):
    initial_guess = n/2

    for _ in range(10):
        initial_guess = 0.5 * (initial_guess + (n/initial_guess))

    return initial_guess

def main():

    print(mySqrt(327))
if __name__ == '__main__':
    main()