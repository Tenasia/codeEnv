
from string import ascii_letters, ascii_lowercase

def mapLetter(alphabet):

    new_alphabet = ''
    for i in alphabet:
        new_alphabet = i + new_alphabet
    
    return new_alphabet

def subCiph(message, mapped_letters):
    alphabet = ascii_lowercase
    new_message = ''
    for i in message:
        if i in mapped_letters:
            a = alphabet.find(i)
            b = mapped_letters[a]
            new_message += b
    return new_message

def decCiph(encrypted_message, mapped_letters):
    alphabet = ascii_lowercase
    new_message = ''
    for i in encrypted_message:
        if i in alphabet:
            a = mapped_letters.find(i)
            b = alphabet[a]
            new_message += b
    return new_message

def main():
    a = mapLetter(ascii_lowercase)


    b = subCiph('hehehehehe', a)
    print(b)

    c = decCiph(b, a)
    print(c)

if __name__ == '__main__':
    main()