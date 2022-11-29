
from audioop import reverse


def reverse(str):
    string = str
    newstring = ''
    for chr in string:
        newstring = chr + newstring
    
    return f'{string}, {newstring}'

def main():
    
    a = reverse('hallo')
    print(a)

    

if __name__ == '__main__':
    main()