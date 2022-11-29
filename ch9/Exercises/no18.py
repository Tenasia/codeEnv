

from string import ascii_lowercase


def rot13(string):
    alphabet = ascii_lowercase
    new_str = ''
    for i in string:
        if i == ' ':
            new_str += ' '
        else:
            rotated_index = (alphabet.index(i) + 13) % 26
            new_str += alphabet[rotated_index]

    return new_str


def main():
    print(rot13(rot13('since test')))


if __name__ == '__main__':
    main()