from sys import prefix


def main():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for p in prefixes:
        if p == 'O' or p == 'Q':
            print(f'{p}u{suffix}')
        else:
            print(p + suffix)
    

if __name__ == '__main__':
    main()