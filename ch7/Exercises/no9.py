
def is_odd(n):
    return not(is_even(n))

def is_even(n):
    return n % 2 == 0

def main():
    print(is_odd(7))
    print(is_odd(10))

if __name__ == '__main__':
    main()