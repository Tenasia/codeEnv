
import string


def main():
    numbers = string.digits
    print(numbers)
    iter = input('input an integer')

    integerinInt = 0
    for i in iter:
        if i in numbers:
            integerinInt += 1
    print(integerinInt)


if __name__ == '__main__':
    main()