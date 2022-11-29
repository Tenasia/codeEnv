
def isLeap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else: 
            return True
    else:
        return False
        

def main():
    print(isLeap(400))


if __name__ == '__main__':
    main()