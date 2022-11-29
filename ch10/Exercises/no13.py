
def replace(string, old, new):

    string_split = string.split(old)
    
    replaced_string = new.join(string_split)

    return replaced_string




def main():
    a = replace('Mississippi', 'i', 'I')
    print(a)
if __name__ == '__main__':
    main()