def is_righangled1(a, b, c):

    if a > b and a > b:
        a, b, c = b, c, a
    if b > a and b > c:
        a, b, c = a, c, b
    else:
        pass

    result = (a ** 2 + b ** 2) - c ** 2

    print(result)

    if abs(result) < 0.001:
        return True
    else: 
        return False


def main():

    a = is_righangled1(1, 4, 5)
    print(a)


if __name__ == '__main__':
    main()